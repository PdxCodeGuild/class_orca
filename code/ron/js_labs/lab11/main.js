
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

// Global variables, arrays, etc. ---------------------------------

    /* None */ 
 
// Declarations---------------------------------------------------

    /* None */ 

// Code------------------------------------------------------------

var app = new Vue({

    el: '#todoApp',     //'el' is element name to ref in html

  //Data
    data: {

      //temp storage for items to be added to todoList             
      add: '',

      //Data array for items
      todoList: [
        { id: 1,
          todoItem: 'Learn Vue',
          completed: false }, 
        { id: 2 ,
          todoItem: 'Cardio',
          completed: false }, 
        { id: 3 ,
          todoItem: 'Pushups',
          completed: true }, 
      ]
    },

  //Functions
    methods: {
      
        //Add items to Current Item list (i.e. Array)
        addItem: function () {
          this.todoList.push({
            id: this.todoList.length+1,
            todoItem: this.add,
            completed: false,
          });
        this.add = ''; //reset input
        },

        //Move items to complete list
        completeItem: function(list){
          list.completed = !list.completed;
        },

        //Delete items from lists and array
        removeItem: function(list){
          var index = _.findIndex(this.todoList, list);
          this.todoList.splice(index, 1);
        },
    },

}) // end 'app'


// Buttons and Events-----------------------------------------------

    /* None */ 

// End code