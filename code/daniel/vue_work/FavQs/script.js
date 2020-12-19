let vm = new Vue({
    el: "#quoteApp",                              
    data: {                                       
        quotes: [],  
        temp_keyphrase: "",                             
        keyphrase: "",                            
        searchtype: "",
        last_page: null,
        page: 1,
        temp_page: null
    },
    created: function () {
        for (let i=0; i<3; i++) {
        this.getRandomQuotes()
        }
    },
    methods: { 
        getRandomQuotes: function() {
            axios({
                url: "https://favqs.com/api/qotd",
                method: "get",
                headers: {
                    "Authorization": 'Token token="56c614fcaacbd765f67886b20e05301d"'
                },
            }).then(response => {
                this.quotes.push(response.data.quote) 
            })
        },                                   
        getQuotes: function() {
            axios({
                url: "https://favqs.com/api/quotes",
                method: "get",
                headers: {
                    "Authorization": 'Token token="56c614fcaacbd765f67886b20e05301d"'
                },
                params: {
                    type: this.searchtype,
                    filter: this.keyphrase,
                    page: this.page,
                }
            }).then(response => {
                this.quotes = response.data.quotes
                this.page = response.data.page
                this.last_page = response.data.last_page
            })
        },
        nextPage: function() {
            this.page++
            this.getQuotes() 
        },
        previousPage: function () {
            this.page--
            this.getQuotes()
        },
    },
}) 