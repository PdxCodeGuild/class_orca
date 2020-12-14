Vue.component('todo-item', {
    data: function() {
        return {

        }
    },
    props: ['todo'],
    template: `
    <li>
        <input type="checkbox" v-model="todo.completed">
        {{ todo.text }}
        <button @click="removeTodo(todo, $event)">×</button>
    </li>
    `
})

let vm = new Vue({
    el: "#app",
    data: {
        todos: [],
        newTodoText: "",
        newTodoId: 1
    },
    methods: {
        addTodo: function() {
            this.todos.push({ text: this.newTodoText, completed: false, id: this.newTodoId })
            this.newTodoId++
            this.newTodoText = ""
        },
        removeTodo: function(todo, event) {
            console.log(event)
            this.todos.splice(this.todos.indexOf(todo), 1)
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
        }
    }
})

// let vm = new Vue({
//     el: "#app",
//     data: {
//         todos: [],
//         newTodoText: "",
//         newTodoId: 1
//     },
//     methods: {
//         addTodo: function() {
//             this.todos.push({ text: this.newTodoText, completed: false, id: this.newTodoId })
//             this.newTodoId++
//             this.newTodoText = ""
//         },
//         removeTodo: function(todo, event) {
//             console.log(event)
//             this.todos.splice(this.todos.indexOf(todo), 1)
//         }
//     },
//     computed: {
//         incompleteTodos: function() {
//             return this.todos.filter(function(todo) {
//                 return todo.completed === false
//             })
//         },
//         completeTodos: function() {
//             return this.todos.filter(function(todo) {
//                 return todo.completed === true
//             })
//         }
//     }
// })