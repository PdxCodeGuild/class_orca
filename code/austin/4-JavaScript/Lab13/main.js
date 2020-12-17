Vue.component('total', {
    props: [
        "total",
    ],
    template: `
    <p>Total results: {{ total }}
    </p>
    `
});  

let vm = new Vue ({
    el: '#app',
    data: {
        quotes: [],
        rando_quotes: [],
        searchTerm: "",
        page: 1,
        lastPage: false,
        key: "",
    },
    computed: {
        total: function() {
            return this.quotes.length
        }
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
                    page: this.page,
                    last_page: this.lastPage
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
                    type: "tag",
                    page: this.page

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
                    type: "author",
                    page: this.page

                }
            }).then(response => {
                this.quotes = response.data.quotes
            })
        },
        loadQuoteRandom: function() {
            for (let i = 0; i < 3; i++) {
                axios({
                    url: "https://favqs.com/api/qotd",
                    method: "get",
                    headers: {
                    "Authorization": `Token token="${apiKey}"`
                    },
                }).then(response => {
                    this.rando_quotes.push(response.data.quote)
                    
                })
            }
        },
        prevPage: function() {
            this.page--,
            this.loadQuote()
        },

        nextPage: function() {
            this.page++
            this.loadQuote()
        },
        
        getTotal: function() {
            total = this.quotes.length
            console.log(total, "TOTAL")
        } 
    },
    created() {
        this.loadQuoteRandom()
    },
    updated() {
        this.getTotal()
    }
})

