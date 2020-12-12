
let vm = new Vue({
    el: '#app', 
    data: {
        task: "",
        tasks: ['Make egg nog'],
        doneTasks: [],
        isComplete: false
    },
    methods: {
        addTask: function() {
            this.tasks.push(this.task)
            this.task = " "
        },
        markDone: function(task, index) {
            this.doneTasks.push(task)
            this.tasks.splice(index, 1)
        },
        deleteTask: function(index) {
            this.tasks.splice(index, 1)
        },
    } 
});
