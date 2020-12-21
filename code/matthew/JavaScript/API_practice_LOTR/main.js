var vm = new Vue({
    el: '#app',
    data: {
        characters: [],
    },
    methods: {
        charList: function(){
            axios({
                url: `https://the-one-api.dev/v2/character`,
                method: "get",
                headers: {
                    Authorization: 'Bearer YDHob91N5Ls52iBVgljK'
                },
            }).then(response => {
                console.log(response.data)
                this.characters = response.data.docs
            })
        },
        quotes: function(character){
            console.log(character)
            axios({
                url: `https://the-one-api.dev/v2/character/${character._id}/quote`,
                method: "get",
                headers: {
                    Authorization: 'Bearer YDHob91N5Ls52iBVgljK'
                },      
            }).then(response => {
                // console.log(response.data)
                character.quotes = response.data.docs
                console.log(this.characters)
            })
        }   
    }
})