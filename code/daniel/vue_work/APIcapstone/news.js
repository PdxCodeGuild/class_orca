Vue.component("news-app",{
    template: `
    <div id="news-articles">
        <div id="load-news">
            <button type="submit" @click="getArticles(); showNews = !showNews">Get the latest news!</button>
        </div>

        <div class="article" v-for="article in top_stories" :key="article.url" v-show="showNews" >
            <div id="article-media">
                <img :src="article.multimedia[0].url" style="height: 175px">
                <p id="caption">{{ article.multimedia[0].caption }}"</p>
                <p id="author-text">Photographed by: </p><p id="author">{{ article.multimedia[0].copyright }}</p>
            </div>
            <div id="article-text">
                <h2>{{ article.title }}</h2>
                <p><a :href="article.url">{{ article.abstract }}</a></p>
                <p id="author-text">Authored by: </p><p id="author">{{ article.byline }}</p>
            </div> 
        </div>
    </div>
    `,
    data: function () {
        return {
        sectionText: "us",
        top_stories: [],
        showNews: false,
        }
    },
    methods: {
        getArticles: function () {
            axios({
                url: `https://api.nytimes.com/svc/topstories/v2/${this.sectionText}.json`,
                method: "get",
                params: {
                    "api-key": "2NIyW8Rh76YvWvhqxWW4CHExZTXqY4dP"
                }
            }).then(response => {
                this.top_stories = []
                for (let i=0; i<5; i++) {
                    this.top_stories.push(response.data.results[i])
                }
                console.log(response, this.top_stories)
            })
        }
    }
})