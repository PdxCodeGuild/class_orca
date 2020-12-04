

// Usually put these at the top (like declaring variables)
let btn = document.getElementById("btn");
let more = document.getElementById("more");
let inputs = document.getElementById("inputs")
let nums = document.getElementsByClassName("num")
let results = document.getElementById("results");

let numCounter = 2;  // Counter for input input elements

// Below used to explicitly call input elements vs. dynamically by class
// let num1 = document.getElementById("num1");
// let num2 = document.getElementById("num2");

// Below code changed to an explict function
// btn.addEventListener('click', function(e) {

function doMath(e) {
    let li = document.createElement("li");
    let num = document.getElementsByClassName("num");
    let sum = 0;
    for (let i = 0; i < nums.length; i++) {
        if (nums[i].value) {
            sum += parseFloat(nums[i].value);
        };
    };
    li.innerText = sum;
    results.appendChild(li);
    // Below used for simple input 
    // li.innerText = `${nums[0].value} + ${nums[1].value} = ${parseFloat(nums[0].value) + parseFloat(nums[1].value)}`;
};

// This is the btn to call the function doMath (i.e. changed from above code)
btn.addEventListener('click', doMath);

more.addEventListener('click', function(e) {
    //Creates input elements dynamically
    let newInput = document.createElement("input");
    newInput.type = "number";
    newInput.placeholder = `number ${numCounter +=1}`;
    newInput.classList.add("num");

    newInput.addEventListener('input', function(e) {
        //Super cool to show value in console
        console.log(this.value);
    });
    
    newInput.addEventListener('keydown', function(e) {
        if (e.key === "Enter") {
            doMath(e);
        };
    });

    // newInput.addEventListener('keydown', function(e) {
    //     //Super cool to show value in console
    //     console.log(e.key);
    // });

    // newInput.addEventListener('input', doMath);

    //Below: adds an x to delete input fields
    let btn = document.createElement("button")
    btn.innerText = "x";
    //Good example of the function "remembering" the context of itself
    btn.addEventListener('click', function(e){
        this.previousSibling.remove();    // 'this' refers to the item left of the addEventList
        this.nextSibling.remove();
        this.remove();
    });

    inputs.append(' + ');
    inputs.appendChild(newInput);
    inputs.appendChild(btn)

});

// console.log(nums)

////////////////////////////////////////////////////////////////

let dot = document.getElementById("dot");
let box = document.getElementById("box");

let mouse_down = false;

box.addEventListener("mousemove", function(e) {
    if (mouse_down) {
        dot.style.left = (e.clientX - 8) + "px";
        dot.style.top = (e.clientY - 8) + "px";
    }
});

box.addEventListener("mousedown", function(e) {
    mouse_down = true;
});

box.addEventListener("mouseup", function(e) {
    mouse_down = false;
});