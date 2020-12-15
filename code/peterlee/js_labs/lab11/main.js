let vm = new Vue({
  el: "#todoapp",
  data: {
  	todos: [{text: 'Example', done: false, id: Date.now()}]
  },

  methods: {
  	addTodo({target}){
    	this.todos.push({text: target.value, done: false, id: Date.now()})
      target.value = ''
    },

    
    removeTodo(id) {
    	this.todos = this.todos.filter(todo => todo.id !== id)
    }
  }
})