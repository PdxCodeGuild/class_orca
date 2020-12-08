var listCounter = 0;

let addDiv = document.getElementById("adddiv");
let inputField = document.getElementById("inputfield");
let addBtn = document.getElementById("addbtn");
let toDoUL = document.getElementById("todoul");
let toDoListDiv = document.getElementById("todolistdiv");

addBtn.addEventListener("click", function(e) {
    let addItem = document.createElement("LI");
    addItem.id = "item" + listCounter;
    addItem.innerText = inputField.value;

    let removeBtn = document.createElement("button");
    removeBtn.innerText = "Remove";
    removeBtn.id = "removebtn";

    let markComplete = document.createElement("button");
    markComplete.innerText = "Mark Complete";
    markComplete.id = "markcompletebtn";

    addItem.appendChild(removeBtn);
    addItem.appendChild(markComplete);
    toDoUL.appendChild(addItem);
    listCounter++;
});

document.addEventListener('click', function(e) {
    if (e.target.id=="removebtn") {
        let deleteItem = this.parentNode;
        deleteItem.removeChild();
    }
});