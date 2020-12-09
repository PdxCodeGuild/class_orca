let listtodo = document.getElementById("listtodo");
let completelist = document.getElementById("completelist");
let add = document.getElementById("add");
let task = document.getElementById("task")

// let newtask = document.createElement('li')
//     newtask.innerText = `${task.value} `
//     newtask.setAttribute('class', 'newtask')
//     newtask.setAttribute('id', task.value)
//     console.log(newtask.id)
    
// let completebutton = document.createElement('input')
//     completebutton.setAttribute('type', 'button')
//     completebutton.setAttribute('value', '✓')
//     completebutton.style.width = '25px'
//     completebutton.style.height = '25px'
//     completebutton.style.color = 'green'
    
// let deletebutton = document.createElement('input')
//     deletebutton.setAttribute('type', 'button')
//     deletebutton.setAttribute('value', 'x')
//     deletebutton.style.width = '25px'
//     deletebutton.style.height = '25px'
//     deletebutton.style.color = 'red'


add.addEventListener("click", function(){
    // console.log(parseInt(number.value))
    console.log("add works!")
    let newtask = document.createElement('li')
    newtask.innerText = `${task.value} `
    newtask.setAttribute('class', 'newtask')
    newtask.setAttribute('id', task.value)
    console.log(newtask.id)
    listtodo.appendChild(newtask)
    let completebutton = document.createElement('input')
    completebutton.onclick = ()=> completebuttonpush(newtask.id)
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
})

const completebuttonpush = function(anything){

    let completetask = document.createElement('li')
    completetask.setAttribute('class', 'newtask')
    completetask.setAttribute('id', anything)
    // console.log(event)
    completetask.innerText =`${anything} `
    completetask.style.textDecoration = "line-through"
    completelist.appendChild(completetask)
    
    let uncompletebutton = document.createElement('input')
    uncompletebutton.onclick = ()=> uncompletebuttonpush(completetask.id)
    // uncompletebutton.onclick = ()=> completebuttonpush(newtask.id)
    uncompletebutton.setAttribute('type', 'button')
    uncompletebutton.setAttribute('value', '⚬')
    
    // completebutton.innerText = '✓'
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
    //     }
    // else if( deleteitem in completelist){
    //     completelist.removeChild(deleteitem)
    //     }
    }

    const deletebuttonpush2 = function(anything){
        let deleteitem = document.getElementById(anything)
        console.log("I made it here too")
        console.log(anything, deleteitem)
    
        // if(document.getElementById(deleteitem) listtodo){
        //    listtodo.removeChild(deleteitem)
        //     }
    
        completelist.removeChild(deleteitem)
        //     }
        }

        let uncompletebuttonpush = function(anything){
            undelete = document.getAnimations(anything)
            completelist.removeChild(undelete)


        }
