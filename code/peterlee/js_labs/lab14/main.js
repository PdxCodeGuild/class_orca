let vm = new Vue({
    el: '#app',
    data: {
        stocks: "",
        search: "",
        searched: false,
        daily: "",
        dailyButton: true,
        weekly: "",
        weeklyButton: true,
        monthly: "",
        monthlyButton: true
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
                    this.searched = true;
                }) 
        },

        getDaily: function () {
            axios({
                url: "https://www.alphavantage.co/query?",
                method: "get",
                params: {
                    function: "TIME_SERIES_DAILY_ADJUSTED",
                    symbol: this.search,
                    outputsize: "compact",
                    apikey: `${apiKey}`
                }
            }). then(response => {
                this.daily = response.data;
                this.dailyButton = false;
            })
        },

        getWeekly: function () {
            axios({
                url: "https://www.alphavantage.co/query?",
                method: "get",
                params: {
                    function: "TIME_SERIES_WEEKLY_ADJUSTED",
                    symbol: this.search,
                    outputsize: "compact",
                    apikey: `${apiKey}`
                }
            }). then(response => {
                this.weekly = response.data;
                this.weeklyButton = false;
            })
        },


        getMonth: function () {
            axios({
                url: "https://www.alphavantage.co/query?",
                method: "get",
                params: {
                    function: "TIME_SERIES_MONTHLY_ADJUSTED",
                    symbol: this.search,
                    outputsize: "compact",
                    apikey: `${apiKey}`
                }
            }). then(response => {
                this.monthly = response.data;
                this.monthlyButton = false;
            })
        }
    }
})