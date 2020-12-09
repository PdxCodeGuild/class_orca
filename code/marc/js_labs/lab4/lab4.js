//This is Lab 4. A to do list. I made it more convuluted by using nodes instead of an array
//it does have a working "un-complete" button.

let listtodo = document.getElementById("listtodo");
let completelist = document.getElementById("completelist");
let add = document.getElementById("add");
let task = document.getElementById("task")



add.addEventListener("click", function(){
    addtask = task.value
    console.log("inside addnewtask")
    createNewTask(addtask)  
})

let createNewTask = function(addtask){
    // console.log(parseInt(number.value))
    console.log(addtask)
    console.log("add works!")
    let newtask = document.createElement('li')
    newtask.innerText = `${addtask} `
    newtask.setAttribute('class', 'newtask')
    newtask.setAttribute('id', `${addtask}`)
    console.log(newtask.id, "newtask id?")
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
    task.value = ''
}

const completebuttonpush = function(anything){

    let completetask = document.createElement('li')
    completetask.setAttribute('class', 'newtask')
    completetask.setAttribute('id', anything)
    // console.log(event)
    completetask.innerText =`${anything} `
    completetask.style.textDecoration = "line-through"
    completelist.appendChild(completetask)
    
    let uncompletebutton = document.createElement('input')
    console.log(completetask.id, "this is completetaskid")
    // uncompletebutton.onclick = ()=> uncompletebuttonpush(completetask.id)
    let y = completetask.id 
    let x = function(y){
    console.log ("it got to here")
    remove = document.getElementById(y)
    completelist.removeChild(remove)
    console.log(y, "this should be anything")
    createNewTask(y)  
          
    }
    uncompletebutton.onclick = ()=> x(y)
    uncompletebutton.setAttribute('type', 'button')
    uncompletebutton.setAttribute('value', '⚬')
    uncompletebutton.style.width = '25px'
    uncompletebutton.style.height = '25px'
    uncompletebutton.style.color = 'green'
    let deletebutton = document.createElement('input')
    deletebutton.onclick = ()=> deletebuttonpush2(completetask.id)
    deletebutton.setAttribute('type', 'button')
    deletebutton.setAttribute('value', 'x')
    deletebutton.style.width = '25px'
    deletebutton.style.height = '25px'
    deletebutton.style.color = 'red'
    completetask.appendChild(uncompletebutton)
    completetask.appendChild(deletebutton)
    let deleted = document.getElementById(anything)
    listtodo.removeChild(deleted)

    console.log(completetask)
}

const deletebuttonpush = function(anything){
    let deleteitem = document.getElementById(anything)
    console.log("it made it here")
    console.log(anything, deleteitem)
    listtodo.removeChild(deleteitem)
   
    }

const deletebuttonpush2 = function(anything){
    let deleteitem = document.getElementById(anything)
    console.log("I made it here too")
    console.log(anything, deleteitem)
    completelist.removeChild(deleteitem)
    }

// let uncompletebuttonpush = function(anything){
//     undelete = document.getElementById(anything)
//     completelist.removeChild(undelete)
//     console.log(anything, "this should be anything")
//     createNewTask(anything)  

//     }
