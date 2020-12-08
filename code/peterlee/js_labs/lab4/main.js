var listCounter = 0;

let addDiv = document.getElementById("adddiv");
let inputField = document.getElementById("inputfield");
let addBtn = document.getElementById("addbtn");
let toDoUL = document.getElementById("todoul");
let toDoListDiv = document.getElementById("todolistdiv");
let completedUL = document.getElementById("completedul");

let removeItems = document.getElementsByClassName("remove");

function remove() {
    this.parentNode.parentNode.removeChild(this.parentNode);
}

function markComplete() {
    completedUL.appendChild(this.parentNode);
    this.remove();

}

addBtn.addEventListener("click", function(e) {
    let addItem = document.createElement("LI");
    addItem.id = "item" + listCounter;
    addItem.innerText = inputField.value;

    let removeBtn = document.createElement("button");
    removeBtn.innerText = "Remove";
    removeBtn.id = "removebtn";
    removeBtn.classList = "remove";

    let markCompleteBtn = document.createElement("button");
    markCompleteBtn.innerText = "Mark Complete";
    markCompleteBtn.id = "markcompletebtn";

    addItem.appendChild(removeBtn);
    addItem.appendChild(markCompleteBtn);
    toDoUL.appendChild(addItem);
    listCounter++;

    removeBtn.addEventListener("click", remove);
    markCompleteBtn.addEventListener("click", markComplete);


});

