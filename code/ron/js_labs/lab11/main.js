
//  *'-.-'*'-.-'*'-.-'*-.-'*-.-'*-.-'*-.-'*'-.-'*'-.-'*'-.-'*
//         Project: Javascript & Vue
//  Assignment/Ver: Lab 7
//          Author: Ron Mansolilli, ron.mansolilli@gmail.com
//            Date: 12-10-2020
//  *'-.-'*'-.-'*'-.-'*-.-'*-.-'*-.-'*-.-'*'-.-'*'-.-'*'-.-'*

// ----Instructions and notes--------------------------------

    /* To List (JS & Vue)

    Notes:
    1. Store an array of objects (the todos themselves)
    2. List each todo
    3. Allow the user to add and remove todos
    4. Allow a user to toggle if a task is complete or not

    */

// ----Global variables, arrays, etc. ------------------

    /* None */ 
 
// ----Functions----------------------------------------------




// Declarations---------------------------------------------------

    /* None */ 

// Code------------------------------------------------------------

var app = new Vue({

    el: '#to_do_items',

    //Data
    data: {
      list: [
        { text: 'Learn JavaScript' },
        { text: 'Learn Vue' },
        { text: 'Build something awesome' }
      ]
    },

    //Functions
    methods: {
        test: function () {
          this.test = "Testing the function"
        }
    }
  })

  var app6 = new Vue({
    el: '#app-6',
    data: {
      message: 'Hello Vue!'
    }
  })

// Buttons and Events-----------------------------------------------

    /* None */ 

// End code