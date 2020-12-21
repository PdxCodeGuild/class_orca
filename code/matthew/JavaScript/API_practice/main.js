var vm = new Vue({
    el: '#app',
    data: {
        quotes: [],
        searchTerm: ''
    },
    methods: {
        dailyQuotes: function(){
            axios({
                url: "https://favqs.com/api/quotes",
                method: "get",
                headers: {
                    "Authorization": `Token token="5544dc310a6e5c7884b8503cec66a9e6"`
                },
                params: {
                    filter: 'tag',
                    filter: this.searchTerm,
                    
                }
            }).then(response =>{
                    console.log(response.data)
                    this.quotes = response.data.quotes
                })
        }
    }   
})
