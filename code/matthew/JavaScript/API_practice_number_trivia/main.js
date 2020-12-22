var vm = new Vue({
    el: '#app',
    data: {
        fact: {},
        searchTerm: ''
    },
    methods: {
        randomFact: function(){
            axios({
                url: `http://numbersapi.com/${this.searchTerm}/trivia`,
                method: "get",
                headers: {
                    'Content-Type': 'application/json'
                },
                // params: {
                //     filter: this.searchTerm,
                //     type: 'trivia'
                // }
            }).then(response => {
                console.log(response.data)
                this.fact = response.data
            })
        }
    }
})