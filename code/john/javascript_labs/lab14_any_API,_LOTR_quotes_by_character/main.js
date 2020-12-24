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
        character_array: [
            {
                id: "5cd99d4bde30eff6ebccfd0d",
                name: "Sam",
                max_quotes: 218,
            },
            {
                id: "5cd99d4bde30eff6ebccfc15",
                name: "Frodo",
                max_quotes: 229,
            },
            {
                id: "5cd99d4bde30eff6ebccfc7c",
                name: "Merry",
                max_quotes: 139,
            },
            {
                id: "5cd99d4bde30eff6ebccfe2e",
                name: "Pippin",
                max_quotes: 166,
            },
            {
                id: "5cd99d4bde30eff6ebccfc57",
                name: "Boromir",
                max_quotes: 41,
            },
            {
                id: "5cd99d4bde30eff6ebccfbe6",
                name: "Aragorn",
                max_quotes: 214,
            },
            {
                id: "5cd99d4bde30eff6ebccfd23",
                name: "Gimli",
                max_quotes: 116,
            },
            {
                id: "5cd99d4bde30eff6ebccfd81",
                name: "Legolas",
                max_quotes: 55,
            },
            {
                id: "5cd99d4bde30eff6ebccfea0",
                name: "Gandalf",
                max_quotes: 216,
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
          "5cd9d5a0844dc4c55e47afef": "Mouth of Sauron",
          "": "Mauhúr",          
          "": "",
        },
        quotes_as_objects: {}, // works as [] or {}
        search_terms: "",
        current_page: 1,
        current_quote_limit: 2,
        current_offset: 0,
        current_search_character: "",
        max_quotes: 2390, // 2390 is the API's max quotes, with no character selected
    },
    methods: {
        quotes_search_function: function() {
            // / / / / / / / / / / / / / / / / / WORKING FROM HERE / / / / / / / / / / / / / / / / / / / / / / / / /
            console.log(`quotes_search_function()`)
            axios({
                method: 'get',
                url: 'https://the-one-api.dev/v2/quote',
                // url: 'https://the-one-api.dev/v2/chapter/5cdc25d5bc17e929cf246219/',
                headers: {
                    Authorization: `Bearer ${apiKey}` // secrets.js: var apiKey 
                },
                params: {
                    limit: this.current_quote_limit, // of 2300 movie quotes total, (limit default is 1,000)
                    // page: this.current_page, // (limit default is 10)
                    offset: this.current_offset, //max ~ // offset overwrites page, so pages don't work... (limit default is 10)
                }
            }).then(response => { 
                // console.log(response.data.docs)
                console.log(response.data)
                this.quotes_as_objects = response.data.docs
                // COULD DEFINETLY IMPROVE HOW I'M STORING THE QUOTES RECEIVED...
            // check /movie response...
            // then using hobbit...
            // /movie/{id}/quote says only LOTR... try
            // /quote/{id}
            // / / / / / / / / / / / / / / / / / ^^^^^^^^^ TO HERE / / / / / / / / / / / / / / / / / / / / / / / / /
            })
        },
        // there are no 'pages' on the results here, so we have to calculate using the limit (max quotes returned) and the current offset
        quotes_search_function_by_character: function(char_object) {
            // axios/call section comments are above in initial axios function
            console.log(`quotes_search_function(character) characterID=${char_object.id} and char_object.max_quotes: ${char_object.max_quotes}`)
            this.current_search_character = char_object.id
            this.max_quotes = char_object.max_quotes
            this.current_offset = this.set_random_offset()
            console.log(`logging line 136 current_offset: ${this.current_offset}`)
            axios({
                method: 'get',
                url: 'https://the-one-api.dev/v2/character/' + this.current_search_character + '/quote/', //concatenates the char ID into the URL string, per API docs
                headers: {
                    Authorization: `Bearer ${apiKey}`
                },
                params: {
                    limit: this.current_quote_limit,
                    offset: this.current_offset,
                }
            }).then(response => { 
                console.log(response.data)
                this.quotes_as_objects = response.data.docs
            })
        },
        page_forward: function() {
            console.log(`logging start of function: page_forward(), current_page: ${this.current_page}, current_offset: ${this.current_offset}, current_quote_limit: ${this.current_quote_limit}`)
            this.current_offset += this.current_quote_limit
            this.quotes_search_function()
        },
        page_backward: function() {
            console.log(`logging start of function: page_backward(), current_page: ${this.current_page}, current_offset: ${this.current_offset}, current_quote_limit: ${this.current_quote_limit}`)     
            this.current_offset -= this.current_quote_limit
            this.quotes_search_function()
        },
        set_random_offset: function() { //used JS lab2b__pick_6 for help:
            console.log(`set_random_offset() START with this.max_quotes: ${this.max_quotes}`)
            var random_number = Math.random()
            random_int_max = Math.floor(random_number * Math.floor(this.max_quotes))
            this.current_offset = random_int_max
            console.log(`set_random_offset() END with this.current_offset: ${this.current_offset}`)
            return random_int_max
        },
        get_random_quote: function() { //used JS lab2b__pick_6 for help:
            console.log(`get_random_quote() START`)
            this.max_quotes = 2390
            this.current_offset = this.set_random_offset()
            this.quotes_search_function()
            console.log(`get_random_quote() END}`)
        },        
        reset_search: function() {
            console.log(`reset_search()`)
            // currently not used in HTML
            // probably want to reset these two: 
            this.max_quotes = 2390
            this.current_quote_limit = 2
            this.current_search_character = ""
            this.get_random_quote()
        },
        set_current_quote_limit: function() {
            // console.log(input_number)
            console.log(`OLD this.current_quote_limit: ${this.current_quote_limit}`)
            // this.current_quote_limit = input_number
            // IMPORTANT NOTE event.target.value might be what i need in the future
            // console.log(`set_current_quote_limit to: ${input_number}`)
            // console.log(`set_current_quote_limit to: ${n}`)
            console.log(`NEW this.current_quote_limit: ${this.current_quote_limit}`)
        },
    },
    mounted:function() {
        this.max_quotes = 2390
        this.set_random_offset()
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