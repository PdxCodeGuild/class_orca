// ##############################################################################
// # John Fial, PDX Code Guild, 2020-2021, www.johnfial.com
    // # PROJECT: JS LAB 14, ANY API: 
    // # Start with LOTR Quote, add interactivity and CSS, then add depth...
    // # potentially other API calls connected to that LOTR quote/page (or user input)...
    // https://the-one-api.dev/documentation
// / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
new Vue({
    el: '#tolkien_quotes',
    data: {
        quotes_as_objects: {},
        quote_random: {},
        search_terms: "",
        current_page: 1,
        current_limit: 2,
        current_offset: 1,
        //
        character_array: [
            {
                id: "5cd99d4bde30eff6ebccfd0d",
                name: "Sam",
            },
            {
                id: "5cd99d4bde30eff6ebccfc15",
                name: "Frodo",
            },
            {
                id: "5cd99d4bde30eff6ebccfc7c",
                name: "Merry",
            },
            {
                id: "5cd99d4bde30eff6ebccfe2e",
                name: "Pippin",
            },
            {
                id: "5cd99d4bde30eff6ebccfc57",
                name: "Boromir",
            },
            {
                id: "5cd99d4bde30eff6ebccfbe6",
                name: "Aragorn",
            },
            {
                id: "5cd99d4bde30eff6ebccfd23",
                name: "Gimli",
            },
            {
                id: "5cd99d4bde30eff6ebccfd81",
                name: "Legolas",
            },
            {
                id: "5cd99d4bde30eff6ebccfea0",
                name: "Gandalf",
            }
        ],
        character_ids_and_names: {
          "5cd99d4bde30eff6ebccfd0d": "Sam", // 218 quotes
          "5cd99d4bde30eff6ebccfc15": "Frodo", // 229 quotes
          "5cd99d4bde30eff6ebccfc7c": "Merry", // 139 quotes
          "5cd99d4bde30eff6ebccfe2e": "Pippin", // 166 quotes, https://lotr.fandom.com/wiki/Peregrin_Took
          "5cd99d4bde30eff6ebccfc57": "Boromir", // 41 quotes
          "5cd99d4bde30eff6ebccfbe6": "Aragorn", // 214
          "5cd99d4bde30eff6ebccfd23": "Gimli", // 116 quotes
          "5cd99d4bde30eff6ebccfd81": "Legolas", // 55 quotes
          "5cd99d4bde30eff6ebccfea0": "Gandalf", // 216 quotes
          //
          "5cd99d4bde30eff6ebccfe9e": "Gollum/Smeagol",
          "5cd99d4bde30eff6ebccfc38": "Bilbo",
          "5cd99d4bde30eff6ebccfd06": "Galadriel",
          "5cd99d4bde30eff6ebccfcc8": "Elrond",
          "5cd9d576844dc4c55e47afee": "Agmar",
          //
          "5cd99d4bde30eff6ebccfe19": "Theoden",
          "5cd99d4bde30eff6ebccfcef": "Faramir",
          "5cd9d533844dc4c55e47afed": "Treebeard",
          "5cd99d4bde30eff6ebccfca7": "Deagol",
          "5cd99d4bde30eff6ebccfca1": "Denethor",
          "5cd99d4bde30eff6ebccfc07": "Arwen",
          "5cdbdecb6dc0baeae48cfa59": "Èowyn",
          "5cdbdecb6dc0baeae48cfa5a": "Èomer",
          "5cd99d4bde30eff6ebccfe9d": "Gríma",
          "5cd99d4bde30eff6ebccfea5": "Sauron",
          "5cdbe49b7ed9587226e794a0": "Hero Orc",
          "5cd99d4bde30eff6ebccfea4": "Saruman",
          "5cdbdecb6dc0baeae48cfa96": "Gothmog",
          "5cd99d4bde30eff6ebccfd0e": "Gamling",
          "5cdbdecb6dc0baeae48cfab2": "Uglúk",
          "": "Mauhúr",
          "": "",
        },
    },
    methods: {
        quotes_search_function: function(search_terms, characterID="quote") {
            console.log(`quotes_search_function(search_terms, character="") ${search_terms}, character=${characterID}`)
            console.log('https://the-one-api.dev/v2/character/'+characterID+'/quote/')
// / / / / / / / / / / / / / / / / / WORKING FROM HERE / / / / / / / / / / / / / / / / / / / / / / / / /
            axios({
                method: 'get',
                url: 'https://the-one-api.dev/v2/character/'+characterID+'/quote/',
                // url: 'https://the-one-api.dev/v2/quote',
                // url: 'https://the-one-api.dev/v2/chapter/5cdc25d5bc17e929cf246219/',
                headers: {
                    Authorization: `Bearer ${apiKey}` // secrets.js: var apiKey 
                },
                params: {
                    // filter: search_terms,
                    limit: this.current_limit, // of 2300 movie quotes total, (limit default is 1,000)
                    // page: this.current_page, // (limit default is 10)
                    offset: this.current_offset, //max ~ // offset overwrites page, so pages don't work... (limit default is 10)
                }
            }).then(response => { 
                // console.log(response.data.docs)
                console.log(response.data)
                this.quotes_as_objects = response.data.docs
            })
        },
        page_forward: function(search_terms) {
            console.log(`logging start of function: page_forward(), current_page: ${this.current_page}, current_offset: ${this.current_offset}, current_limit: ${this.current_limit}`)
            // this.current_page ++
            this.current_offset += this.current_limit
            this.quotes_search_function()
        },
        page_backward: function(search_terms) {
            console.log(`logging start of function: page_backward(), current_page: ${this.current_page}, current_offset: ${this.current_offset}, current_limit: ${this.urrent_limit}`)     
            // this.current_page --
            this.current_offset -= this.current_limit
            this.quotes_search_function()
        },
        get_random_quote() { //used JS lab2b__pick_6 for help:
            var random_number = Math.random()
            random_int_max_2390 = Math.floor(random_number * Math.floor(2390))
            console.log(random_int_max_2390)

            this.current_offset = random_int_max_2390
            this.quotes_search_function()
        },
        get_quote_by_character(char_object) {
            console.log(char_object.id)
            console.log(`make a random search BY char ID: ${char_object.id}`)
            this.current_offset = 0
            this.quotes_search_function("",char_object.id)
        },
    },
    // / / / / / / / / / / / / / / / / / ^^^^^^^^^ TO HERE / / / / / / / / / / / / / / / / / / / / / / / / /
    mounted:function(search_terms) {
        console.log('page load!')
        this.get_random_quote()
    },
})

// / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
Vue.component ('component_search', {
    // IGNORE THIS, FOR NOW! 
    // Copied from lab13 the search box...
    data: function() {
        return {
        quotes_as_objects: [],
        search_terms: "",
        }
    },
    template: `
        <div id="search">
            <h3>Search for quotes:</h3>
            <input v-model="search_terms" type="text" placeholder="Ex: cats, Mark Twain, funny..."> Search by: 
            <button v-on:click="$emit('quotes_search_function', search_terms, 'keyword')">*Keyword*</button>
            <button v-on:click="$emit('quotes_search_function', search_terms, 'author')">*Author*</button>
            <button v-on:click="$emit('quotes_search_function', search_terms, 'tag')">*Tag*</button>
            <br>
        </div>
    `,
    methods: {
        }
    },
)
// # NOTES and TODO:
//     ##############################################################################
//     ##############################################################################