
var vm = new Vue({
    el: "#app",
    data: {
        quotes: [],
        searchTerm: "",
    },
 
    methods: {
        loadQuote: function() {
            axios({
                // url: "https://favqs.com/api/qotd",
                url: "https://favqs.com/api/quotes",
                method: "get",
                headers: {
                    // "Authorization": 'Token token="0869e4e2f2664a6852f4b04bd1d51065"',
                    "Authorization": `Token token="${apiKey}"`
                },
                params: {
                    // filter: "Mark Twain",
                    filter: this.searchTerm,
                    type: "author",
                }
            }).then(response => {
                console.log(response.data.quotes)
                this.quotes = response.data.quotes
            
            })
        }
    }
})



