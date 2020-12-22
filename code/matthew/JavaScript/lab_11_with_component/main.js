
Vue.component('add-todo', {

  template: `
    <div>
        <input type="text" placeholder="What do you want to do?" @keyup.enter="addTodo" v-model="text">
        <button @click="addTodo">Add to List</button>
      </div>
      `,
      methods: {
          addTodo: function() {
          this.pendingList.push(this.textInput) 
          this.pendingList.push(textInput.value) 
          }
      }
  })
var app = new Vue({
    el: '#app',
      todos: [],
  },
  methods: {
      addTodo: function(todo) {
          this.todos.push(todo)
      // },
      // removeTodo: function(todo) {
      //     this.todos.splice(this.todos.indexOf(todo), 1)
      // }
  },
    data: {
      pendingList: [],
      completedList: [],
      textInput: '',
  
    },
})


  //   methods: {
  //     appendList: function() {
  //       this.pendingList.push(this.textInput) 
  //       // this.pendingList.push(textInput.value) 
  //     },
  //     deleteBtn: function(index) {
  //       this.pendingList.splice(index, 1)
  //     },
  //     checked: function(index) {
  //       this.completedList.push(this.textInput) 
  //     },
  //     compltedDeleteBtn: function (index) {
  //       this.completedList.splice(index, 1)
  //     }
  //   }
  // })