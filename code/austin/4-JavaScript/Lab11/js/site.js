
let vm = new Vue({
    el: '#app', 
    data: {
        tasks: ['Make egg nog'],
        complete: false,
    },
    methods: {
        addTask: function() {
            this.tasks.push("new task")
        },
    } 
});