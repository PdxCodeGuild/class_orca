Vue.component('todo-item', {
    data: function() {
        return {
            editing: false
        }
    },
    props: ['todo'],
    template: `
    <li>
        <input type="checkbox" v-model="todo.completed">
        <input v-if="editing" type="text" v-model="todo.text" @keyup.enter="toggleEdit">
        <template v-else>{{ todo.text }}</template>
        <button @click="toggleEdit">{{ editing ? "Done" : "Edit" }}</button>
        <button @click="$emit('remove', todo)">×</button>
    </li>
    `,
    methods: {
        toggleEdit: function() {
            this.editing = this.editing ? false : true
        }
    }
})

Vue.component('add-todo', {
    data: function() {
        return {
            text: "",
            id: 1
        }
    },
    template: `
    <div>
        <input type="text" placeholder="What do you want to do?" @keyup.enter="addTodo" v-model="text">
        <button @click="addTodo">Add to List</button>
    </div>
    `,
    methods: {
        addTodo: function() {
            this.$emit('add', { text: this.text, completed: false, id: this.id })
            this.id++
            this.text = ""
        }
    }
})

let vm = new Vue({
    el: "#app",
    data: {
        todos: [],
        newTodoText: ""
    },
    methods: {
        addTodo: function(todo){
            this.todos.push(todo)
            this.newTodoText = ""
        },
        removeTodo: function(todo) {
            this.todos.splice(this.todos.indexOf(todo), 1)
        }
    },
    computed: {
        incompleteTodos: function(){
            return this.todos.filter(function(todo) {
                return todo.completed === false
            })
        }
    }
})