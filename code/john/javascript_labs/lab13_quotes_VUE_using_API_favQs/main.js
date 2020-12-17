
// / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
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
            <input v-model="search_terms" type="text" placeholder="Ex: cats, Twain, funny, philosophy, etc.">
            <button v-on:click="$emit('quotes_search_function', search_terms)">Search by *Keyword*</button>
            <button v-on:click="$emit('quotes_search_function', search_terms)">Search by *Author*</button>
            <button v-on:click="$emit('quotes_search_function', search_terms)">Search by *Tag*</button>
            <br>
            <button><-- Page (Disabled button)</button>
            <button>(Disabled button) Page --></button>
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
        page: 1
    },
    methods: {
        quotes_search_function: function(search_terms) {
            console.log(`logging this line 27! input search_terms: ${search_terms}`)
            axios({
                method: 'get',
                url: 'https://favqs.com/api/quotes', //had to change from /quotes ... why?
                headers: {
                    // Authorization: Token token=apiKey // secrets.js: var apiKey
                    "Authorization": `Token token="${apiKey}"`
                },
                params: {
                    // filter: this.search_terms,
                    // type: 'tag', // input
                    // page: 1, // need to fix this... lots of werk here!
                }
            }).then(response => { 
                console.log(response.data.quotes)
                this.quotes_as_objects = response.data.quotes
            })
        },
        search_by_keyword: function(search_terms){
            console.log(`running search_by_keyword() with search_terms ${search_terms}`)
            quotes_search_function(search_terms)
        },
        search_by_author: function(search_terms){
            console.log(`running search_by_author() with search_terms ${search_terms}`)
            quotes_search_function(search_terms)
        },
        search_by_tag: function(search_terms){
            console.log(`running search_by_tag() with search_terms ${search_terms}`)
            quotes_search_function(search_terms)
        },
    },
    mounted:function() {
        console.log('page load!')
        this.quotes_search_function()
    },
})


// / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /



// / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / /
// Build a Vue application that allows a user to search for quotes on FavQs.
// Requirements:
//     Your app must use Vue to fetch data and interact with the results.
//     Let the user enter a search term and select whether to search by keyword, author, or tag.
//     Implement pagination buttons when the search returns more than 25 quotes.
//     When the page first loads, show the user a set of completely random quotes.
//     You must have at least one Vue component in your app.
// Resources:
//     FavQs API
//     Vue documentation
//     Using Axios to Consume APIs
//     Axios documentation
// Hints:
//     Read the API documentation!
//     Remember to use your Vue app data as your single source of truth.
//     You'll need to set the Authorization header for the FavQs API to work.