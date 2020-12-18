 
//  *'-.-'*'-.-'*'-.-'*-.-'*-.-'*-.-'*-.-'*'-.-'*'-.-'*'-.-'*
//         Project: Javascript & Vue
//  Assignment/Ver: Lab 13
//          Author: Ron Mansolilli, ron.mansolilli@gmail.com
//            Date: 12-15-2020
//  *'-.-'*'-.-'*'-.-'*-.-'*-.-'*-.-'*-.-'*'-.-'*'-.-'*'-.-'*

// ----Instructions and notes--------------------------------

    /* Famous Quote Page/App (JS, Vue, & Axios)

    Notes:

    1. Your app must use Vue to fetch data and interact with the 
    results. (complete)
    2. Let the user enter a search term and select whether to 
    search by keyword, author, or tag. (complete)
    3. Implement pagination buttons when the search returns more 
    than 25 quotes.
    4. When the page first loads, show the user a set of completely 
    random quotes.
    5. You must have at least one Vue component in your app.

    */

// Global variables, arrays, etc. ---------------------------------

    /* None */ 
 
// Declarations---------------------------------------------------

    /* None */ 

// Code------------------------------------------------------------

var app = new Vue({

    el: '#quoteApp',     //'el' is element name to ref in html

  //Data
    data: {

      //temp data storage             
      search_text: '',
      search_type: 'keyword',
      //Data array for quotes
      quotes: [],
      //Random variables 
      num: 1,
      current_page: 1,
    },

  //Methods
    methods: {
      
      //Return quotes based on Search Button
      loadQuote: function() {
        axios({
            // url: "https://favqs.com/api/qotd",
            url: "https://favqs.com/api/quotes",
            method: "get",
            headers: {
                "Authorization": `Token token="${apiKey}"`
            },
            params: {
                filter: this.search_text,
                type: this.search_type,
                page: this.current_page,
            },
        }).then(response => {
            console.log(response.data.quotes),
            this.quotes = response.data.quotes       
            })
        },

      firstQuote: function() {
        axios({
            url: "https://favqs.com/api/quotes",
            method: "get",
            headers: {
                "Authorization": `Token token="${apiKey}"`
            },
            params: {
              // None //
            },
        }).then(response => {
            console.log(response.data.quotes),
            this.quotes = response.data.quotes       
            })
        },
      
      nextPage: function() {
        console.log("hi")
        this.current_page++
        this.loadQuote()
      },

      previousPage: function() {
        this.current_page--
        this.loadQuote()
      }
    },

  // Initial load of quotes (on page initialization)
    created() {

      console.log('created called.');
      this.firstQuote();

    },

})

