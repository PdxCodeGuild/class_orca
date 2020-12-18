var vm = new Vue({
    el: '#app',
    data: {
        searchTerm: '',
        imageReturned: [],
        collectionReturned: [],
        albumGallery: [],
        show: false,
        ori: 'landscape',
        page: 1,
        oriCheck: true,
        current: 'red',
    },
    methods: {
        search: function(){
             // check if the current term is the search term and do following 
            if (this.searchTerm !== this.current){
                this.current = this.searchTerm
                // assign page number to 1 so when using forward and back button the value resets
                this.page = 1
                // call the axios for the search called axiosCall
                this.axiosCall()
            }
            else {
            // call the axios function without needing to reset the page 
            this.collectionReturned = []
            this.albumGallery = []
            this.axiosCall()
        }
        },
        // axios was made into a function so it can be used in the search function
        axiosCall: function(){
            axios({
                url: `https://api.unsplash.com/search/photos`,
                method: "get",
                headers: {
                    Authorization: 'Client-ID LXt7SKNT81SzuL1hSgEb_ikc_Via3sqx5TGWq_ZjpX4',
                },
                params: {
                    query: this.current,
                    page: this.page,
                    per_page: 30,
                    orientation: this.ori,
                }
            }).then(response =>{
                this.imageReturned = response.data.results
            })
        },
        collection: function(){
            // reset imageReturned and albumGallery to an empty array so the other pictures or albums will not stay on page
            this.imageReturned = []
            this.albumGallery = []
            console.log(this.searchTerm)
            axios({
                url: `https://api.unsplash.com/collections`,
                method: "get",
                headers: {
                    Authorization: 'Client-ID LXt7SKNT81SzuL1hSgEb_ikc_Via3sqx5TGWq_ZjpX4',
                },
                params: {
                    query: this.searchTerm,
                    page: 1,
                    per_page: 90,
                }
            }).then(response =>{
                console.log(response.data)
                this.page = 1
                this.show = true
                this.collectionReturned = response.data
            })  
        },
        // pass the album though the function. Give a true/false value to display or remove appearance
        viewAlbum: function(collection) {
            this.page = 1
            this.show = false
            this.albumGallery = collection
            console.log(this.albumGallery)   
        },
        // function for next page button
        nextPage: function() {
            console.log()
            this.page++ 
            this.search()
            },
        // function for next previous button
        lastPage: function() {
            this.page--
            this.search()
        },
    }
})