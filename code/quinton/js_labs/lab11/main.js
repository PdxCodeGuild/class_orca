const app = new Vue ({
    el: '#todo_app',
    data() {
        return {
            newToDo: '',
            existingToDo: [],
            doneToDo: []
        }
    },
    methods:{
        add(){
            this.existingToDo.push({
                text: this.newToDo
            }),
            this.newToDo = ''
        },
        deleteIncompleteToDo(i){
            console.log(i)
            this.existingToDo.splice(i, 1)
        },
        deleteCompleteToDo(i){
            this.doneToDo.splice(i, 1)
        },
        completeToDo(i){
            const done = this.existingToDo.splice(i, 1)
            this.doneToDo.push({
                text: done[0].text
            })
        }
    }
})