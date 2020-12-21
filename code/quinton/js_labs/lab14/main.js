new Vue({
    el:"#app",
    data: {
        searchTerm: '',
        current: '',
        movie: {},
        favorites: [],
        showFavorites: false,

    },
    methods: {
        getMovie: function () {
            console.log(this.searchTerm)
            axios({
                url: "http://www.omdbapi.com/",
                method: 'get',
                params: {
                    apikey: apiKey,
                    t: this.current,
                    plot: 'full'
                }
            }).then(response => {
                this.movie = response.data
            })
        },
        addToFavorites: function() {
            this.favorites.push(this.movie)
            console.log(this.favorites)
        },
        favoritesToggle: function() {
            this.showFavorites = true
        },
        checkMovie: function (something) {
            this.current = something
            console.log(something)
            if (this.current !== this.searchTerm) {
                console.log('made it')
                this.current = this.searchTerm
                this.getMovie()
            } else {
                this.getMovie()
            }
        }
    }
})