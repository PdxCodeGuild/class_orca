var listCounter = 0;

let addDiv = document.getElementById("adddiv");
let inputField = document.getElementById("inputfield");
let addBtn = document.getElementById("addbtn");
let toDoUL = document.getElementById("todoul");
let toDoListDiv = document.getElementById("todolistdiv");
let completedUL = document.getElementById("completedul");
let removeItems = document.getElementsByClassName("remove");


//remove item from either list
function remove() {
    this.parentNode.parentNode.removeChild(this.parentNode);
}


//mark an item complete and move to completed list
function markComplete() {
    completedUL.appendChild(this.parentNode);
    let markIncompleteBtn = document.createElement("button");
    markIncompleteBtn.innerText = "Mark Incomplete";
    this.parentNode.appendChild(markIncompleteBtn);
    this.remove();

    markIncompleteBtn.addEventListener("click", markIncomplete);
}

//mark an item incomplete and move to incomplete list
function markIncomplete() {
    toDoUL.appendChild(this.parentNode);
    let markCompleteBtn = document.createElement("button");
    markCompleteBtn.innerText = "Mark Complete";
    this.parentNode.appendChild(markCompleteBtn);
    this.remove();

    markCompleteBtn.addEventListener("click", markComplete);

}

//adds new items to todolist
addBtn.addEventListener("click", function(e) {
    //new list item
    let addItem = document.createElement("LI");
    addItem.id = "item" + listCounter;
    addItem.innerText = inputField.value;
    //remove button for item
    let removeBtn = document.createElement("button");
    removeBtn.innerText = "Remove";
    //mark complete button for item
    let markCompleteBtn = document.createElement("button");
    markCompleteBtn.innerText = "Mark Complete";
    //adding remove and mark complete buttons to new item
    addItem.appendChild(removeBtn);
    addItem.appendChild(markCompleteBtn);
    //adding item to todo list
    toDoUL.appendChild(addItem);
    listCounter++;
    //adding functionality to newly created remove and mark complete buttons
    removeBtn.addEventListener("click", remove);
    markCompleteBtn.addEventListener("click", markComplete);
});

