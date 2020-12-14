// new Vue({
//     el: '#app',
//     data: {
//         message: 'This is your Todo List'
//     }
// })

// new Vue({
//     el: '#app2',
//     data: {
//         message: 'This is your complete list'
//     }
// })

// let todolist = new Vue({
//     el: '#todolist',
//     data: {
//       todos: [
//         { id: 0, text: 'Learn JavaScript' },
//       ]
    //   methods: {
    //     addToTdo: function () {
    //       this.message = this.message.split('').reverse().join('')
    //     }
//     }
//   })
let vm = new Vue({
    el: '#thewholeapp',
    data: {
      todo: [],
      // completed:[],
      newtask:"",
      id:"",
      thelist: 'This is your Todo List',
      thecompletelist: "This is your Complete List"

  },
  methods:{
      addNewTask: function(){
          let newtask = {
              text:`${this.newtask} `,
              id:`${this.newtask}`,
              complete : false,
            }; this.todo.push(newtask),
            this.newtask=''
      
          console.log(this.newtask)
       },
       completeTask: function(id){
        console.log('you are in complete')
        this.todo[id].complete = true
        // this.completed.push(this.todo[id])   
        // this.todo.pop(this.todo[id])
         },
       uncompleteTask: function(id){
           console.log("you are in incomplete")
           this.completedList[id].complete = false
          //  this.todo.push(this.completed[id])
          //  this.completed.pop(this.completed[id])  
       },
       deleteTask: function(id){
           console.log("you are in delete")
           this.todo.pop(this.todo[id])
        
    } 
},
  computed:{
           completedList: function(){
           return this.todo.filter(function(item){
           return item.complete 
           })
          },
           
           todoList: function(){
            return this.todo.filter(function(item){
            return item.complete == false
            })
          }          
        }
  
  
})