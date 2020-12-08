let container = document.getElementById("container")
let listForm = document.getElementById("item_generator")
let completed_items = document.getElementById("completed_items")
let list = document.createElement("div")

let add_item = document.createElement("input")
add_item.setAttribute("type", "text")
add_item.setAttribute("placeholder", " Add Item")
container.appendChild(add_item)



let submit = document.createElement("input")
submit.setAttribute("type", "button")
submit.setAttribute("value", "Submit")
container.appendChild(submit)

submit.addEventListener('click', function (event) {
    
    let item_bucket = document.createElement("div")
    let item = document.createElement("p")
    item_bucket.id = add_item.value
    let complete = document.createElement("input")
    complete.setAttribute("type", "button")
    complete.setAttribute("value", "COMPLETE")
    complete.addEventListener('click', function () {
        item.style.textDecorationLine = "line-through"
        completed_items.appendChild(item)
        completed_items.appendChild(delete_item)
        item_bucket.remove()
    })
    let delete_item = document.createElement("input")
    delete_item.setAttribute("type", "button")
    delete_item.setAttribute("value", "DELETE")
    delete_item.addEventListener("click", function () {
        item.remove()
        delete_item.remove()
        item_bucket.remove()

    })
    item.innerText = add_item.value
    item_bucket.appendChild(complete)
    item_bucket.appendChild(delete_item)
    item_bucket.appendChild(item)
    listForm.appendChild(item_bucket)
    add_item.value=''
})
