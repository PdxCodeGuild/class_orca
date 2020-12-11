



// Your Vue app will need to do a few things:

// Store an array of objects (the todos themselves)
// List each todo
// Allow the user to add and remove todos
// Allow a user to toggle if a task is complete or not

// C:\-=Cloud=-\Sync\git_working\week9_javascript\lab11_to_do_list_in_JS-VUE



const vm = new Vue({
    el: '#welcome',
    data: { 
      // message: 'Hello Vue!' // most important part, where 'state' lives
      tasks: ['apples', 'pears', 'banananas', ],
      tasks2: []
    } // can't even put a semicolon here!
  });


  const todolist = new Vue({
    el: '#app2',
    data: { 
      message: 'Hello00000 Vue!',
      tasks: ['apples', 'pears', 'banananas', ],
    },
    methods: {
      sayHello: function() {
        tasks.push(this.message);
      }
    }
  });

// NOTES: 
// data and methods are going to use the same NAMESPACE, so don't use same variable names...
// “TypeError: Vue is not a constructor” when starting out their JS file?

// From Merritt Lawrenson to Everyone:  02:38 PM
// Watch your syntax and make sure your script tag for vue comes before your script tag for your JS file






// // NOTES FROM MERRIT'S REVIEW OF THIS ON THURS, 10 DEC 2020:
// function addTodoCallback() {
//     const todoText = 
//     // remove button:
//         // remove parent element
//     // TO-DO LOOKUP JAVASCRIPT 'this'
// };
// // END THOSE NOTES