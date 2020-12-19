new Vue ({
    el:'#app',
    data : {
        freebies: [],
        key: '',
        game: ''
    },    
    methods: {
        filterGames : function () {
            axios({
                url: 'https://cors-anywhere.herokuapp.com/https://www.gamerpower.com/api/giveaways',
                method: 'get',
                params: {
                    platform : this.key
                }
            }).then (response => {
                console.log(response.data)
                this.freebies = response.data
            })
        },
        platformSelect(event) {
            key = event.target.value
            this.filterGames()
            // console.log(key, 'platform')
        },
        removeGame(game) {
            console.log(game)
            console.log(this.freebies)
            this.freebies.splice(this.freebies.indexOf(game),1)
        }
    },
    mounted : function () {
        axios({
            url: 'https://cors-anywhere.herokuapp.com/https://www.gamerpower.com/api/giveaways',
            method: 'get',
        })
        .then (response => {
            this.freebies = response.data
        })
    }
})


////////////////////////////////////
// headers: 'Access-Control-Allow-Origin: *'


/////////////////////////////////////////
// new Vue ({
//     el:'#app',
//     data : {
//         freebies: [],
//         key: ''
//     },    
//     mounted : function () {
//         axios({
//             url: 'https://cors-anywhere.herokuapp.com/https://pixabay.com/api/',
//             method: 'get',
//             headers: {
//                 "Authorization": `Token token="${APIkey}"`
//             }
//         })
//         .then (response => {
//             this.freebies = response.data
//         })
//     }
// })