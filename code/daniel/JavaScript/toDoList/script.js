// Global variables
let item_generator = document.getElementById("item_generator")
let todo_list = document.getElementById("todo_list")
let completed_list = document.getElementById("completed_list")

// User input
let input_container = document.createElement("p")
input_container.id = "add_item"
let input_field = document.createElement("input")
input_field.setAttribute("type", "text")
input_field.setAttribute("placeholder", " Enter item")
input_container.appendChild(input_field)
item_generator.appendChild(input_container)

// Submit button
let submit_btn = document.createElement("p")
submit_btn.id = "add_item"
let submit_event = document.createElement("input")
submit_event.setAttribute("type", "button")
submit_event.setAttribute("value", "Submit")
submit_btn.appendChild(submit_event)
item_generator.appendChild(submit_btn)
input_field.onkeypress = function (e) {
    if (e.key === "Enter") {
        add_item()
    }
}
submit_event.onclick = add_item

// Additem to Todo List
function add_item () {

    // New div for added item
    let todo_item = document.createElement("div")
    todo_item.className = "item"
    let item = document.createElement("p")
    item.innerText = input_field.value
    let created_on = document.createElement("p")
    created_on.innerText = "created on: "+todays_date()

    // Delete button
    let delete_btn = document.createElement("p")
    let delete_event = document.createElement("input")
    delete_event.setAttribute("type", "button")
    delete_event.setAttribute("value", "Delete")
    delete_btn.appendChild(delete_event) 
    delete_event.onclick = function () {
        todo_list.removeChild(todo_item)
    } 

    // Complete button
    let complete_btn = document.createElement("p")
    let complete_event = document.createElement("input")
    complete_event.setAttribute("type", "button")
    complete_event.setAttribute("value", "Complete")
    complete_btn.appendChild(complete_event)
    complete_event.onclick = function () {
        complete_item(created_on, todo_item, complete_btn, delete_btn)
    }

    // Append elements
    todo_item.appendChild(item)
    todo_item.appendChild(created_on)
    todo_item.appendChild(complete_btn)
    todo_item.appendChild(delete_btn) 
    todo_list.appendChild(todo_item)
    input_field.value = ''
} 

// Complete an item
function complete_item (created_on, todo_item, complete_btn, delete_btn) {
    let completed_on = document.createElement("p")
    completed_on.innerText = "completed on: "+todays_date()
    todo_item.appendChild(completed_on)
    completed_list.appendChild(todo_item)
    todo_item.removeChild(complete_btn, delete_btn)
    
    let add_again_btn = document.createElement("p")
    let add_again_event = document.createElement("input")
    add_again_event.setAttribute("type", "button")
    add_again_event.setAttribute("value", "Add Again")
    add_again_btn.appendChild(add_again_event)
    todo_item.appendChild(add_again_btn)
    add_again_btn.onclick = function () {
        todo_item.removeChild(completed_on)
        created_on.innerText = "created on: "+todays_date()
        add_again_btn.remove()
        delete_btn.remove()
        todo_item.appendChild(complete_btn)
        todo_item.appendChild(delete_btn)
        todo_list.appendChild(todo_item)
    }
    todo_item.appendChild(delete_btn)
    delete_btn.onclick = function () {
        completed_list.removeChild(todo_item)
    }
}

// Today's date
function todays_date () {
    let today = new Date()
    let day = today.getDate()
    let month = today.getMonth()+1
    let year = today.getFullYear()
    let date = document.createElement("p")
    return (`${month}/${day}/${year}`)
}