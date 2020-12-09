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

toDoDiv.style.border = "2px solid darkblue"
toDoDiv.style.width = "30%"
toDoDiv.style.minHeight = "700px"
toDoDiv.style.marginLeft = "350px"
toDoDiv.style.backgroundImage = "url('paper.jpg')"

toDoTitle.style.textDecoration = "underline"
toDoTitle.style.fontSize = "30px"
toDoTitle.style.marginLeft = "50px"
toDoTitle.style.textAlign = "center"

toDoList.style.alignContent = "center"
toDoList.style.width = "60%"
toDoList.style.marginLeft = "auto"
toDoList.style.marginRight = "auto"
toDoList.style.paddingTop = "15px"


title.style.textAlign = "center"
title.style.fontSize = "60px"

addItemDiv.style.display = "flex"
addItemDiv.style.justifyContent = "center"

document.body.style.color = "black"
document.body.style.backgroundImage = "url('todobg.jpg')"
document.body.style.backgroundRepeat = "no-repeat";
document.body.style.backgroundSize = "cover";
document.body.style.fontFamily = "'Roboto', sans-serif"

inputTaskBtn.style.fontSize = "24px"
inputTaskBtn.style.border = "2px solid darkblue"
inputTaskBtn.style.borderRadius = "10px"

completedList.style.marginLeft = "100px"
completedList.style.justifySelf = "center"
completedList.style.paddingTop = "15px"

completedDiv.style.marginRight = "350px"
completedDiv.style.backgroundImage = "url('paper.jpg')"

completedTitle.style.fontSize = "30px"
completedTitle.style.textDecoration = "underline"
completedTitle.style.marginLeft = "50px"
completedTitle.style.textAlign = "center"

completedDiv.style.border = "2px solid darkblue"
completedDiv.style.width = "30%"





inputTaskBtn.addEventListener('click', function() {
    let userInput = prompt('What task would you like to add to the list?')
    let toDoItem = document.createElement("li")
    
    const completedBtn = document.createElement("button")
    completedBtn.setAttribute('id', 'completedBtn')
    completedBtn.innerText = "Complete"
    completedBtn.style.fontSize = "16px"
    completedBtn.style.margin = "auto"
    completedBtn.style.marginBottom = "15px"
    
    let deleteBtn = document.createElement('button')
    deleteBtn.setAttribute('id', 'deleteBtn')
    deleteBtn.innerText = "Delete"
    deleteBtn.style.fontSize = "16px"
    
    toDoItem.innerText = userInput
    toDoList.appendChild(toDoItem)
    toDoItem.append("       ")
    toDoItem.appendChild(completedBtn)
    toDoItem.append("    ")
    toDoItem.appendChild(deleteBtn)
    console.log(toDoItem)
    
    toDoItem.style.fontSize = "30px"
    toDoItem.style.fontFamily = "'Shadows Into Light', cursive"
    
    
    
    
    
    completedBtn.addEventListener('click', function(){
        let completedItem = completedBtn.parentElement
        // var n = event.timeStamp
        toDoList.removeChild(completedItem)
        completedList.append(completedItem)
        completedBtn.remove()
        toDoItem.style.textDecoration = "line-through"
        
        // let time = document.createElement('span')
        // time.setAttribute("id", "time")
        // completedList.appendChild(time)
        // var dt = new Date();
        // document.getElementById("time").innerHTML = (("0"+(dt.getMonth()+1)).slice(-2)) +"/"+ (("0"+dt.getDate()).slice(-2)) +"/"+ (dt.getFullYear())
        // time.appendChild(dt)

        })
        
        deleteBtn.addEventListener('click', function() {
            let deletedItem = deleteBtn.parentElement
            toDoItem.remove()
            time.remove()
        })
    })
    