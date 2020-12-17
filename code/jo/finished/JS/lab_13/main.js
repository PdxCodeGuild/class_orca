Vue.component ('next-page', {
    template: `<button @click="$emit('nextpage')" type='button'>Next Page</button>` 
    // `<button @click="$emit('firstpage')" type='button'>First Page</button>`
})

new Vue ({
    el:'#app',
    data : {
        quotes: [],
        search: '',
        key: '',
        page: 1,
        last_page: false
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
                    type: this.key,
                    filter: this.search,
                    page: this.page
                }
            }).then (response => {
                this.quotes = response.data.quotes,
                this.page = response.data.page,
                this.last_page = response.data.last_page
            })
        },
        termSelect(event) {
            key = event.target.value
        },
        firstPage: function () {
            this.page = 1
        },
        nextPage: function () {
            this.page += 1
            this.loadQuote()
        },
        previosPage: function () {
            this.page -= 1
        }
    },
    mounted : function () {
        axios({
            url: 'https://favqs.com/api/quotes',
                method: 'get',
                headers: {
                    "Authorization": `Token token="${APIkey}"`
                },
        })
        .then (response => {
            this.quotes = response.data.quotes
        })
    },
})



///////////////////////
    // mounted : function () {
    //     this.loadQuote()
    // },

    // created(){
    //     this.loadQuote()
    // }
//////////////////////////




    // mounted () {
    //     axios
    //         .get("https://favqs.com/api/quotes"),
    //         headers {
    //             "Authorization": token='4ce456320793100ccdc918247b30641c'
    //         },
    //         .then(response => (this.info = response.data.quotes))
    // }