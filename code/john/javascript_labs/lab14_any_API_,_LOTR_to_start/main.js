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
        search_terms: "",
        page: 1,
    },
    methods: {
        quotes_search_function: function(search_terms) {
            console.log(`logging start of function: quotes_search_function(search_terms)`)
            // if (this.search_terms === false ) {
            //     this.search_terms = ""
            // }

// / / / / / / / / / / / / / / / / / WORKING FROM HERE / / / / / / / / / / / / / / / / / / / / / / / / /
            axios({
                method: 'get',
                url: 'https://the-one-api.dev/v2/quote',
                headers: {
                    Authorization: `Bearer ${apiKey}` // secrets.js: var apiKey 
                },
                params: {
                    // filter: search_terms,
                    // type: type,
                    // page: this.page,
                    offset: 20,
                    limit: 5,
                }
            }).then(response => { 
                console.log(response.data.docs[3])
                this.quotes_as_objects = response.data.docs
// / / / / / / / / / / / / / / / / / ^^^^^^^^^ TO HERE / / / / / / / / / / / / / / / / / / / / / / / / /
            })
        },
        page_forward: function() {
            console.log(`logging start of function: page_forward()`)
            this.page ++
            //then do the search function...
        },
        page_backward: function() {
            console.log(`logging start of function: page_backward()`)     
            this.page --
            //then do the search function...
        },
    },
    mounted:function() {
        console.log('page load!')
        this.quotes_search_function("")
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