let vm = new Vue({
  el: '#app',
  data: {
    quotes: [],
    search: ""
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
                filter: this.search
            }
            }). then(response => {
            this.quotes = response.data.quotes
            })

        }
    }
})

