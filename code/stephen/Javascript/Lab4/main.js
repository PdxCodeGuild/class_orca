const title = document.getElementById('title')
const toDoDiv = document.getElementById('toDoDiv')
const toDoHead = document.getElementById('toDoHead')
const toDoBody = document.getElementById('toDoBody')
const completedDiv = document.getElementById('completedDiv')
const completedHead = document.getElementById('completedHead')
const completedBody = document.getElementById('completedBody')
const inputTaskBtn = document.getElementById('inputTaskBtn')
const toDoList = document.getElementById('toDoList')
const completedList = document.getElementById('completedList')
const main = document.getElementById('main')
const toDoTitle = document.getElementById('toDoTitle')
const completedTitle = document.getElementById('completedTitle')
const addItemDiv = document.getElementById('addItemDiv')

main.style.display = 'flex'
main.style.justifyContent = "space-around"
completedDiv.style.border = "1px solid black"
toDoDiv.style.border = "1px solid black"
toDoDiv.style.width = "40%"
toDoHead.style.flexDirection = "row"
completedDiv.style.width = "40%"
toDoDiv.style.minHeight = "500px"
toDoTitle.style.textAlign = "center"
completedTitle.style.textAlign = "center"
title.style.textAlign = "center"
addItemDiv.style.display = "flex"
addItemDiv.style.justifyContent = "center"
toDoList.style.alignContent = "center"
document.body.style.color = "wheat"
document.body.style.backgroundColor = "darkgreen"



inputTaskBtn.addEventListener('click', function() {
    let userInput = prompt('What task would you like to add to the list?')
    let toDoItem = document.createElement("li")
    const completedBtn = document.createElement("button")
    completedBtn.setAttribute('id', 'completedBtn')
    completedBtn.innerText = "Complete"
    let deleteBtn = document.createElement('button')
    deleteBtn.setAttribute('id', 'deleteBtn')
    deleteBtn.innerText = "Delete"
    toDoItem.innerText = userInput
    toDoList.appendChild(toDoItem)
    toDoItem.appendChild(completedBtn)
    toDoItem.appendChild(deleteBtn)
    console.log(toDoItem)
    
    
    completedBtn.addEventListener('click', function(){
        let completedItem = completedBtn.parentElement
        toDoList.removeChild(completedItem)
        completedList.append(completedItem)
        completedBtn.remove()
        toDoItem.style.textDecoration = "line-through"
        
        })
        
        deleteBtn.addEventListener('click', function() {
            let deletedItem = deleteBtn.parentElement
            
            toDoItem.remove()
        })
    })
    