Vue.component ('component_search', {
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
// / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
new Vue({
    el: '#app_quotes',
    data: {
        quotes_as_objects: [],
        search_terms: "",
        current_page: 1,
        last_page: false,
    },
    methods: {
        quotes_search_function: function(search_terms, type="") {
            console.log(`logging start of function: quotes_search_function(search_terms), search_terms: ${this.search_terms}`)
            axios({
                method: 'get',
                url: 'https://favqs.com/api/quotes',
                headers: {
                    "Authorization": `Token token="${apiKey}"` // secrets.js: var apiKey
                },
                params: {
                    filter: search_terms,
                    type: type,
                    page: this.page,
                }
            }).then(response => { 
                console.log(`response.data.page: ${response.data.page}, response.data.last_page: ${response.data.last_page}, this.page: ${this.page}`)
                this.quotes_as_objects = response.data.quotes
                this.last_page = response.data.last_page
            })
        },
        page_forward: function() {
            console.log(`logging start of function: page_forward()`)
            this.current_page ++
            this.quotes_search_function()
        },
        page_backward: function() {
            console.log(`logging start of function: page_backward()`)     
            this.current_page --
            this.quotes_search_function()
        },
    },
    mounted:function() {
        // console.log('page load!')
        this.quotes_search_function()
    },
})

// / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
// / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
        // don't need this junk if i'm passing in the search TYPE by the component emitter!
        // search_by_keyword: function(search_terms, ){
        //     console.log(`running search_by_keyword() with search_terms ${search_terms}`)
        //     quotes_search_function(search_terms)
        // },
        // search_by_author: function(search_terms){
        //     console.log(`running search_by_author() with search_terms ${search_terms}`)
        //     quotes_search_function(search_terms)
        // },
        // search_by_tag: function(search_terms){
        //     console.log(`running search_by_tag() with search_terms ${search_terms}`)
        //     quotes_search_function(search_terms)