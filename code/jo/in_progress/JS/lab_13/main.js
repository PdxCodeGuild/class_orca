new Vue ({
    el:'#app',
    data : {
        quotes: [],
        search: '',
        searchedyet: 0,
        key: ''
    },
    methods : {
        loadQuote: function () {
            axios({
                url: 'https://favqs.com/api/quotes',
                method: 'get',
                headers: {
                    "Authorization": `Token token="${APIkey}"`
                },
                params: {
                    filter: this.search
                }
            }).then(response => {this.quotes = response.data.quotes}),
            this.searchedyet++
        },
        selectTerm(event) {
            console.log(event.target.value)
        }
    }
})


    // mounted () {
    //     axios
    //         .get("https://favqs.com/api/quotes"),
    //         headers {
    //             "Authorization": token='4ce456320793100ccdc918247b30641c'
    //         },
    //         .then(response => (this.info = response.data.quotes))
    // }