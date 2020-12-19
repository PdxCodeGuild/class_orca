let vm_news = new Vue({
    el: "#news-app",
    data: {
        top_stories: {},
    },
    created: function () {
        this.getArticles()
    },
    methods: {
        getArticles: function () {
            axios({
                url: `https://api.nytimes.com/svc/topstories/v2/${section}.json`,
                method: "get",
                params: {
                    apikey: "2NIyW8Rh76YvWvhqxWW4CHExZTXqY4dP",
                    section: "home"
                }
            }).then(response => {
                console.log(response)
            })
        }
    }
})