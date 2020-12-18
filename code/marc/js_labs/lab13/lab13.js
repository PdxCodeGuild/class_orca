Vue.component('next-page', {
    data: function() {
        return {
            // pages: 1
            
        }
    },
    props:["pages", "lastpage"],
    
    template: `
    <div>

        <button v-if="pages>=2" @click="$emit('nextpage','backward')">⮜</button>
        <button v-if="!lastpage" @click="$emit('nextpage','forward')">⮞</button>

    </div>`,


    
})


let vm = new Vue({
    el:'#app',

    data:{
        quotes:[],
        searchTerm:'',
        searchby:"keyword",
        pages:1, 
        lastpage: false
        },
        methods: {
            loadQuote: function(evt){

                        // console.log("inside loadQuote", evt.target.textContent)
                        console.log(this.searchTerm)

                        
                        axios({
                        url: "https://favqs.com/api/quotes",
        
                        method: "get",
        
                        headers:{
                          "Authorization": `Token token="a51b4c035f2554ba87f3e30c52f9105e"`
                        },
                        params: {
                                filter: this.searchTerm,
                                type: this.searchby,
                                page:this.pages
        
                        }
                  }).then(response =>{
                      this.quotes = response.data.quotes
                      this.lastpage = response.data.last_page
                      console.log(response.data)
                  }) 
                },
                pageLoadquotes: function(){
                        console.log("inside pageloadQuote")
                        axios({
                        url: "https://favqs.com/api/quotes",
        
                        method: "get",
        
                        headers:{
                          "Authorization": `Token token="a51b4c035f2554ba87f3e30c52f9105e"`
                        },
                        params: {
                                // filter: this.searchTerm,
                                // type: this.searchby,
                                // // page:this.pages
        
                        }
                  }).then(response =>{
                      this.quotes = response.data.quotes
                                            
                  })
                }, searchReset:function(){
                            this.searchTerm = ''
                            this.pages = 1
                },
                nextPage: function(value){
                    if(value=="forward"){
                        console.log("this should work")
                        this.pages+=1
                        this.loadQuote()}
                    else if(value=="backward"){
                        this.pages-=1 
                        this.loadQuote()   
                    }

                }
                              

        },
        created(){ 
            this.pageLoadquotes()
        }
    
    })
    
   


    // created(){ 
    //     this.pageLoadquotes()








        //     loadQuote: function(){
        //         if(this.searchby == "keyword"){
        //             console.log(this.searchTerm, "keyword")
        //             this.loadKeywordQuotes(this.searchTerm)}
        //         else if(searchby == "author"){
        //             console.log(this.searchTerm, "author")
        //             this.loadAuthorQuotes(this.searchTerm)
        //         }
        //         else if(this.searchby == "author"){
        //             console.log(this.searchTerm, "tag")
        //             this.loadTagQuotes(this.searchTerm)
        //         } 
        //     },
        //     loadKeywordQuotes: function(){
        //         console.log("inside axios", this.searchTerm)
        //         axios({
        //               url: "https://favqs.com/api/quotes/",

        //               method: "get",

        //               headers:{
        //                 "Authorization": `Token token="a51b4c035f2554ba87f3e30c52f9105e"`
        //               },
        //               params: {
        //                       filter: this.searchTerm
        //               }
        //         }).then(response =>{
        //             this.quotes = response.data.quotes
        //         })
        //     }, 
        //     loadAuthorQuotes: function(){
        //         axios({
        //         url: "https://favqs.com/api/quotes",

        //         method: "get",

        //         headers:{
        //           "Authorization": `Token token="a51b4c035f2554ba87f3e30c52f9105e"`
        //         },
        //         params: {
        //                 filter: this.searchTerm,
        //                 type: 'author'

        //         }
        //   }).then(response =>{
        //       this.quotes = response.data.quotes
        //   })
        // },
        // loadTagQuotes:function() {
        //     axios({
        //     url: "https://favqs.com/api/quotes",

        //     method: "get",

        //     headers:{
        //     "Authorization": `Token token="a51b4c035f2554ba87f3e30c52f9105e"`
        //     },
        //     params: {
        //             filter: this.searchTerm,
        //             type: 'tag'
        //     }
        //     }).then(response =>{
        //         this.quotes = response.data.quotes
        //     })
        // mounted:{ function(){ console.log("load page")
        //         axios({
        //         url: "https://favqs.com/api/quotes",

        //         created: "get",

        //         headers:{
        //           "Authorization": `Token token="a51b4c035f2554ba87f3e30c52f9105e"`
        //         },
        //         params: {
        //                 // filter: this.searchTerm,
        //                 // type: this.searchby,
        //                 // page:this.pages

        //         }
        //   }).then(response =>{
        //       this.quotes = response.data.quotes
        //       console.log(response)
        //   })