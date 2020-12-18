let vm = new Vue({
    el: '#app',
    data: {
        stocks: null,
        search: ""
    },
    methods: {
        searchStocks: function () {
            axios({
                url: "https://www.alphavantage.co/query?",
                method: "get",
                params: {
                    function: "GLOBAL_QUOTE",
                    symbol: this.search,
                    outputsize: "compact",
                    apikey: `${apiKey}`
                }
                }). then(response => {

                    this.stocks = response.data;
                }) 
        }

    }
        
            
    
})