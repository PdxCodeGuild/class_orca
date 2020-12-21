
let vm = new Vue({
    el: "#app",

    //Data array
    data: {
        todos: [],
        newTodoText: "",
        newTodoId: 1,

    },

    //Functions
    methods: {

        addTodo: function() {
            this.todos.push({ text: this.newTodoText, completed: false, id: this.newTodoId })
            this.newTodoId++
            this.newTodoText = ""
        },
        removeTodo: function() {
            console.log()
            this.todo.slice()
        }
    },

    computed: {

        incompleteTodos: function() {
            return this.todos.filter(function(todo) {
                return todo.completed === false
            })
        },

        completeTodos: function() {
            return this.todos.filter(function(todo) {
                return todo.completed === true
            })
        },
    }
}) 