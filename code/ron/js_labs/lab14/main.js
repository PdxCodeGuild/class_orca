 
//  *'-.-'*'-.-'*'-.-'*-.-'*-.-'*-.-'*-.-'*'-.-'*'-.-'*'-.-'*
//         Project: Javascript & Vue
//  Assignment/Ver: Lab 14
//          Author: Ron Mansolilli, ron.mansolilli@gmail.com
//            Date: 12-18-2020
//  *'-.-'*'-.-'*'-.-'*-.-'*-.-'*-.-'*-.-'*'-.-'*'-.-'*'-.-'*

// ----Instructions and notes--------------------------------

    /* Oregon Affordable Housing Information (JS, Vue, & Axios)

    Notes:

    1. Your app must use Vue to fetch data and interact with the 
    results. 

    */

// Global variables, arrays, etc. ---------------------------------

    /* None */ 
 
// Declarations---------------------------------------------------

    /* None */ 

// Code------------------------------------------------------------

var app = new Vue({

    el: '#housingApp',     //'el' is element name to ref in html

  //Data
    data: {

      //temp data storage             
      select_county: '',
      select_city: '',

      //Data array for quotes
      housingData: [],

      //Random variables 
      num: 1,
      currentPage: 1,

    },

  //Methods
    methods: {
      
      //Load housing info from data.oregon to housingData array
      housingInfo: function() {
        axios({
            url: "https://data.oregon.gov/resource/bq26-qyg4.json",
            method: "GET",
            // dataType: "json",
            data: {
              // "status": "CLOSED",
              "$$app_token": apiKey
            },
            // headers: {
            //     "app_token": apiKey
            // },
            // params: {
            //     //None
            // },
        }).then(response => {
            // console.log(response.data.housingData),
            // console.log("Got the data")
            // console.log(response)
            this.housingData = response.data       
            })
        },

      //   $.ajax({
      //     url: "https://data.oregon.gov/resource/bq26-qyg4.json",
      //     type: "GET",
      //     data: {
      //       "$limit" : 5000,
      //       "$$app_token" : "YOURAPPTOKENHERE"
      //     }
      // }).done(function(data) {
      //   alert("Retrieved " + data.length + " records from the dataset!");
      //   console.log(data);
      // });

  //     firstQuote: function() {
  //       axios({
  //           url: "https://favqs.com/api/quotes",
  //           method: "get",
  //           headers: {
  //               "Authorization": `Token token="${apiKey}"`
  //           },
  //           params: {
  //             // None //
  //           },
  //       }).then(response => {
  //           console.log(response.data.quotes),
  //           this.quotes = response.data.quotes       
  //           })
  //       },
      
  //     nextPage: function() {
  //       console.log("hi")
  //       this.currentPage++
  //       this.loadQuote()
  //     },

  //     previousPage: function() {
  //       this.currentPage--
  //       this.loadQuote()
  //     }
  //   },

    // Initial load housing info (on page initialization)
    },
    created: function() {
      // console.log('Created called.');
      this.housingInfo();
      }

})

