let vm = new Vue({
    el: '#app',
    data: {
        quotes: [],
        searchTerm: "",
        options: ''
    },
    methods: {
        loadQuote: function() {
            axios({
                url: "https://favqs.com/api/quotes",
                method: "get",
                headers: {
                    "Authorization": `Token token=${apiKey}`
                },
                params: {
                    filter: this.searchTerm,
                    type: this.options
                }
            }).then(response => {
                this.quotes = response.data.quotes
            })
        }
    }
})