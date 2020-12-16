let vm = new Vue({
    el: '#app',
    data: {
        quote: {},
        quotes: [],
        searchTerm: '',
        searchType: '',
        searching: false,
        page: 1,
        lastpage: false
    },
    methods: {
        loadQuotes: function() {
            axios({
                url: "https://favqs.com/api/quotes/",
                method: 'GET',
                headers: {
                    "Authorization": `Token token="${apiKey}"`
                },
                params: {
                    filter: this.searchTerm,
                    type: this.searchType,
                    page: this.page
                }
            }).then(response => {
                this.quotes = response.data.quotes
                this.searching = true
                console.log(response.data)
            })
        },
        nextPage: function() {
            this.page = this.page+=1
            console.log(this.page)
            this.loadQuotes()
        },
        previousPage: function() {
            this.page = this.page-=1
            this.loadQuotes()
        }
    },
    mounted: function() {
        for (let i = 0; i < 25; i++) {
            axios({
                method: 'GET',
                url: "https://favqs.com/api/qotd"
            }).then(response => {
                this.quotes.push(response.data.quote)
            })
        }
    }
})