// const tasks = []
let vm = new Vue({
    el: '#main',
    data: {
        toDoList: [],
        completeList: [],
        task: {text: ''}
    },
    methods: {
        addItem() {
            
            let newTask = {
                text: prompt('What task do you need to complete?'),
                
            }
            // console.log(newTask)
            
            this.toDoList.push(newTask)
            // console.log(newTask)
        },
        deleteItem(task) {
            
            this.toDoList.splice(this.toDoList.indexOf(task), 1)

        },
        completeItem(task) {
            let donezo = this.toDoList.splice(this.toDoList.indexOf(task), 1)
            donezo = donezo[0]
            this.completeList.push(donezo)
            
        },
        deleteComplete(task) {
            
            this.completeList.splice(this.completeList.indexOf(task), 1)

        }, 
    }
})
