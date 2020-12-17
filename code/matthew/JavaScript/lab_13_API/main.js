Vue.component('number', {
    props: ['number'],
    template: `
        <span>{{number}}.</span>
        `
})

var vm = new Vue({
    el: '#app',
    data: {
        page: 1,
        quotes: [],
        searchTerm: "",
        author: true,
        tag: true 
    },
    mounted:function(){
        this.daillyQuotes()
    },
    methods: {
        resetPage: function(){
            this.page = 1
        },
        helperLoadQuoteTag: function(){
            this.page = 1
            this.loadQuoteTag()
        },
        helperLoadQuoteAuthor: function() {
            this.page = 1
            this.loadQuoteAuthor()
        },
        daillyQuotes: function(){
            axios({
                url: "https://favqs.com/api/quotes",
                method: "get",
                headers: {
                    "Authorization": `Token token="5544dc310a6e5c7884b8503cec66a9e6"`
                },
                params: {
                    filter: this.quotes,
                }
            }).then(response =>{
                console.log(response.data)
                this.quotes = response.data.quotes
            })
                
        },

        loadQuoteAuthor: function () {
            this.author = true
            this.tag = false
            axios({
                url: "https://favqs.com/api/quotes",
                method: "get",
                headers: {
                    "Authorization": `Token token="5544dc310a6e5c7884b8503cec66a9e6"`
                },
                params: {
                    filter: this.searchTerm,
                    type: 'author',
                    page: this.page
                }
            }).then(response => {
                this.quotes = response.data.quotes
            })
        },
        loadQuoteTag: function () {
            this.tag = true
            this.author = false
            axios({
                url: "https://favqs.com/api/quotes",
                method: "get",
                headers: {
                    "Authorization": `Token token="5544dc310a6e5c7884b8503cec66a9e6"`
                },
                params: {
                    filter: this.searchTerm,
                    type: 'tag',
                    page: this.page
                }
            }).then(response => {
                this.quotes = response.data.quotes
            })
        },
        backPage: function() {
            this.page--
            if (this.author){
                this.loadQuoteAuthor()
            } else if (this.tag){
                this.loadQuoteTag()
            }
        },   
        forwardPage: function() {
            this.page++
            // console.log(this.page, 'forwardPage.ran')

            if (this.author){
                this.loadQuoteAuthor()
            } else if (this.tag){
                this.loadQuoteTag()
            } 
        }
    }
})
