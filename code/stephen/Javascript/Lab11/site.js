
new Vue({
    el: '#inputTaskBtn',
    data: {
        task: '',
        tasks: [],
    },
    methods: {
        addItem
        g() {
            task = prompt('yo this work?')
            console.log(task)
            this.tasks.push(this.task)
            console.log(tasks)
        }    
    }
})
