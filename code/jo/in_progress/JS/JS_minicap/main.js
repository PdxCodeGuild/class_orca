new Vue ({
    el:'#app',
    data : {
        freebies: [],
        key: ''
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
                this.freebies = response.data
            })
        },
        platformSelect(event) {
            key = event.target.value
            this.filterGames()
            console.log(key, 'platform')
        },
        removeGame() {
            
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