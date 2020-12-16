
let vm = new Vue ({
    el: '#app',
    data: {
        quotes: [],
        searchTerm: "",
        page: "",
    },
    methods: {
        loadQuote: function() {
            axios({
                url: "https://favqs.com/api/quotes",
                method: "get",
                headers: {
                    "Authorization": `Token token="${apiKey}"`
                },
                params: {
                    filter: this.searchTerm,
                }
            }).then(response => {
                this.quotes = response.data.quotes
            })    
            searchTerm = ""
        },
        loadQuoteTag: function() {
            axios({
                url: "https://favqs.com/api/quotes",
                method: "get",
                headers: {
                    "Authorization": `Token token="${apiKey}"`
                },
                params: {
                    filter: this.searchTerm,
                    type: "tag"

                }
            }).then(response => {
                this.quotes = response.data.quotes
            })
        },
        loadQuoteAuthor: function() {
            axios({
                url: "https://favqs.com/api/quotes",
                method: "get",
                headers: {
                    "Authorization": `Token token="${apiKey}"`
                },
                params: {
                    filter: this.searchTerm,
                    type: "author"

                }
            }).then(response => {
                this.quotes = response.data.quotes
            })
        }
    }
})

