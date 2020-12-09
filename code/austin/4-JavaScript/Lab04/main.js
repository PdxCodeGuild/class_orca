//Global variables
const listItem = document.getElementById('list-item')
const newItem = document.getElementById('item')
const doneItem = document.getElementById('done-list-item')
const completeButton = document.getElementById('item')

//Add function
let addBtn = document.getElementById("add-box");
addBtn.addEventListener('click', function () {
    console.log(newItem.value)
    if (newItem.value != "") {
        let newLi = document.createElement("li");
        let checkBox = document.createElement("input");
        checkBox.type = "checkbox";
        newLi.appendChild(checkBox);
        newLi.appendChild(document.createTextNode(newItem.value));
        listItem.appendChild(newLi);
        let span = document.createElement("SPAN");
        let x = document.createTextNode("\u00D7");
        span.className = "close";
        span.appendChild(x);
        newLi.appendChild(span);
        for (i = 0; i < close.length; i++) {
            close[i].onclick = function() {
                let div = this.parentElement;
                div.style.display = "none";
            }
        }
        //Toggle completion property
        newItem.value = ""
        newLi.onclick = function() {
            console.log('toggle task completion');
            newLi.classList.toggle('complete');
            if (newLi.classList == 'complete') {
                doneItem.appendChild(newLi)
            }
            else {
                listItem.appendChild(newLi)
            }
        }} else {
        console.log("no input")
    }
}, false);

//Delete function -- "x"
let close = document.getElementsByClassName("close");
let i;
console.log(close)
for (i = 0; i < close.length; i++) {
    close[i].onclick = function() {
    let div = this.parentElement;
    div.style.display = "none";
    }
}

//Mark complete function -- check mark
list.addEventListener('click', function(e) {
    if (e.target.tagName === 'LI') {
    e.target.classList.toggle('checked');
    }
    
}, false);