// var apiKey

console.log('logging this line 3!')

Vue.component ('component_search', {
    data: {
        quotes_as_objects: [],
        search_terms: "",
    },
    template: `
        <div id="search">
            <h3>Search for quotes:</h3>
            <input type="text" @keyup.enter="quotes_search_function" placeholder="Ex: funny, Twain, philosophy, cats, etc.">
        </div>
    `,
    methods: {
        quotes_search_function: function() {
            console.log('logging this line 15!')
            console.log(`with input `)
            axios({
                method: 'get',
                url: 'https://favqs.com/api/quotes',
                header: {
                    "Authorization": `Token token="${apiKey}"`
                },


            }).then({

            })

            // this.$emit()
        }
    },
})

new Vue({
    el: '#app_quotes',
    data: {
        quotes: [],
        search_terms: "",
    },
    methods: {
    },
})
