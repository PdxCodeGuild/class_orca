let listtodo = document.getElementById("listtodo");
let completelist = document.getElementById("completelist");
let add = document.getElementById("add");
let task = document.getElementById("task")
let todo_list = []
let complete_list = []

// let add_new_item = function(){
    add.addEventListener("click", function(){
              todo_list.push(task.value)
              console.log(todo_list)
              makelist()
              task.value = ''
    })

    add.addEventListener("click", function(){
        todo_list.push(task.value)
        console.log(todo_list)
        makelist()
        task.value = ''
})


              
            //   add.onclick = () => makelist()
    
        let makelist = function(){
            let node= document.getElementById("listtodo");
            while (node.firstChild) {
                node.removeChild(listtodo.firstChild);
            }
            todo_list.forEach(function (task) {

            let newtask = document.createElement('li')
            newtask.innerText = `${task} `
            newtask.setAttribute('class', 'newtask')
            newtask.setAttribute('id', `${task}`)
            console.log(task, "newtask id?")

            listtodo.appendChild(newtask)
            let completebutton = document.createElement('input')
            completebutton.onclick = ()=> completebuttonpush(newtask.id) //|| addtask)

            completebutton.setAttribute('type', 'button')
            completebutton.setAttribute('value', '✓')
            // completebutton.innerText = '✓'
            completebutton.style.width = '25px'
            completebutton.style.height = '25px'
            completebutton.style.color = 'green'
            let deletebutton = document.createElement('input')
            deletebutton.onclick = ()=> deletebuttonpush(newtask.id)
            deletebutton.setAttribute('type', 'button')
            deletebutton.setAttribute('value', 'x')
            deletebutton.style.width = '25px'
            deletebutton.style.height = '25px'
            deletebutton.style.color = 'red'
            
            // newtask.insertBefore(completebutton, deletebutton)
            newtask.appendChild(completebutton)
            newtask.appendChild(deletebutton)
            
        
        })
    }
        