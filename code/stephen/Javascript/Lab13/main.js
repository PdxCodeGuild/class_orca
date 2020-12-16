
let vm = new Vue({
    el: '#app',
    data: {
        quote: {},
        quotes: [],
        searchTerm: '',
        searchType: '',
        searching: false,
        page: 1,
        lastpage: false,
        count: 0,
        
    },
    methods: {
        loadQuotes: function() {
            axios({
                url: "https://favqs.com/api/quotes/",
                method: 'GET',
                headers: {
                    "Authorization": `Token token="${apiKey}"`
                },
                params: {
                    filter: this.searchTerm,
                    type: this.searchType,
                    page: this.page
                }
            }).then(response => {
                // if (response.data.last_page = true){
                //     this.lastpage = true
                //     console.log(this.lastpage)
                // } else {
                //     this.lastpage = false
                // }
                this.quotes = response.data.quotes
                this.searching = true
                this.page =  response.data.page
                this.lastpage = response.data.last_page
            
                // console.log(response.data.count)
            })
        },
        pageChange: function() {
            axios({
                url: "https://favqs.com/api/quotes/",
                method: 'GET',
                headers: {
                    "Authorization": `Token token="${apiKey}"`
                },
                params: {
                    filter: this.searchTerm,
                    type: this.searchType,
                    page: this.page,
                    
                    
                }
            }).then(response => {
                this.quotes = response.data.quotes
                this.searching = true
                this.page =  response.data.page
                this.lastpage = response.data.last_page
            })
        },
        // pageChange: function() {
        //     axios({
        //         url: "https://favqs.com/api/typehead/",
        //         method: 'GET',
        //         headers: {
        //             "Authorization": `Token token="${apiKey}"`
        //         },
        //         params: {
        //             count: this.quotes.length
        //         }
        //     }).then(response => {
        //         this.quotes = response.data.quotes
        //         this.searching = true
                
            
        //         console.log(response.data)
        //     })
        // },
        nextPage: function() {
            this.page = this.page+=1
            // console.log(this.page)
            this.pageChange()
            window.scrollTo({ top: 0, behavior: 'smooth' })
        },
        previousPage: function() {
            this.page = this.page-=1
            this.pageChange()
            window.scrollTo({ top: 0, behavior: 'smooth' })
        }
    },
    mounted: function() {
        for (let i = 0; i < 25; i++) {
            axios({
                method: 'GET',
                url: "https://favqs.com/api/qotd"
            }).then(response => {
                this.quotes.push(response.data.quote)
            })
        }
    }
})