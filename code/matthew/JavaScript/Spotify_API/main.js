var vm = new Vue({
    el: '#app',
    data: {
        temp: [],
    },
    methods: {
        play: function(){
            axios({
                url: `https://api.nasa.gov/planetary/apod`,
                method: "get",
                headers: {
                    Authorization: 'PGemkLN1vHQAkyUGag3Ha9cOG2RhkaL4bdK9lG87' 
                },
                params: {
                    date: 'today'
                }
            }).then(response => {
                console.log(response.data)
            })
        }   
    }
})