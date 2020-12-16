// const tasks = []
Vue.component('add-item', {
    data: function() {
        return {
            text: '',
        }
    },
    template: `
    <div id="addItemDiv">
    <button @click="addItem" type="button" id="inputTaskBtn">  ADD AN ITEM  </button>
    </div>
    `,
    methods: {
        addItem: function() {
            this.text = prompt('What task do you need to complete?')
            this.$emit('add', {text: this.text})
            // this.toDoList.push(newTask)


        }
    }
})


let vm = new Vue({
    el: '#main',
    data: {
        toDoList: [],
        completeList: [],
        task: {text: ''}
    },
    methods: {
        // addItem() {
            
        //     let newTask = {
        //         text: prompt('What task do you need to complete?'),
                
        //     }
        //     // console.log(newTask)
            
        //     this.toDoList.push(newTask)
        //     // console.log(newTask)
        // },
        addItem: function(task) {
            this.toDoList.push(task)
        },
        deleteItem(task, index) {
            
            this.toDoList.splice(this.toDoList.indexOf(this.task), 1)

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
