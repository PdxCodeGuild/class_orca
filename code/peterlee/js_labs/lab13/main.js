let vm = new Vue({
  el: '#app',
  data: {
    quotes: [],
    search: "",
    selected: "",
    currentPage: 1,
    },
    methods: {
        getQuote: function() {
            axios({
            url: "https://favqs.com/api/quotes",
            method: "get",
            headers: {
                "Authorization": `Token token="${apiKey}"`
            },
            params: {
                filter: this.search,
                type: this.selected,
                page: this.currentPage
            }
            }). then(response => {
                this.quotes = response.data.quotes
            })

        },
        nextPage: function() {
            this.currentPage++
            this.getQuote()
        },
        previousPage: function() {
            this.currentPage--
            this.getQuote()
        }
    }
})

