const incomplete = document.getElementById("incomplete");
const complete = document.getElementById("complete");
const newTodoInput = document.getElementById("newTodoInput");
const addTodoBtn = document.getElementById("addTodoBtn");


function addTodoCallback() {
    const todoText = newTodoInput.value;
    const li = document.createElement("li");

    const removeBtn = document.createElement("button")
    removeBtn.innerText = "-";
    removeBtn.addEventListener("click", function() {
        this.parentElement.remove();
    });

    const completeBtn = document.createElement("button")
    completeBtn.innerText = "-";
    completeBtn.addEventListener("click", function() {
        incomplete.appendChild(this.parentElement);
        this.parentElement.style.textDecoration = "Line-Through";
    });



    const li = document.createElement("li");
    li.append(todoText);
    incomplete.appendChild(li);


}

addTodoBtn.addEventListener("click", addTodoCallback);  // notice that this just has event listener here calling function
