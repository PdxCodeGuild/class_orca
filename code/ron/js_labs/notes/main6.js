


    // let bt = document.querySelector('#bt');
    // bt.addEventListener('click', function() {
    //     alert('hello world!');
    // });


// The Function!
function callback(event) {
    if (event.button === 0) {
        alert("You clicked the left mouse button!");
    } else if (event.button === 2) {
        alert("You clicked the right mouse button!");
    } else {
        alert("You clicked a mouse button, but it wasn't the left or right!");
    }
}

// Declare and addEventListener!  Note: the action and the response (callback to function)
let bt = document.querySelector('#bt');
bt.addEventListener('click', callback);

// Usually put these at the top (like declaring variables)
let btn = document.getElementById("btn");
let more = document.getElementById("more");
let inputs = document.getElementById("inputs")
let numCounter = 2;

// let num1 = document.getElementById("num1");
// let num2 = document.getElementById("num2");
let nums = document.getElementsByClassName("num")
let results = document.getElementById("results");


btn.addEventListener('click', function(e) {
    let li = document.createElement("li");
    let num = document.getElementsByClassName("num");
    console.log(nums);
    let sum = 0;
    for (let i = 0; i < nums.length; i++) {
        if (nums[i].value) {
            sum += parseFloat(nums[i].value);
        };
    };
    li.innerText = sum;
    // Below used for simple input 
    // li.innerText = `${nums[0].value} + ${nums[1].value} = ${parseFloat(nums[0].value) + parseFloat(nums[1].value)}`;
    results.appendChild(li);

});

btn.addEventListener('click', doMath);

more.addEventListener('click', function(e) {
    let newInput = document.createElement("input");
    newInput.type = "number";
    newInput.placeholder = `number ${numCounter +=1}`;
    newInput.classList.add("num");

    newInput.addEventListener('input', function(e) {
        //Super cool to show value in console
        console.log(this.value);
    });
    
    newInput.addEventListener('keydown', function(e) {
        if (e.key === "enter") {
            doMath(e);
        };
    });

    // newInput.addEventListener('keydown', function(e) {
    //     //Super cool to show value in console
    //     console.log(e.key);
    // });

    // newInput.addEventListener('input', doMath);

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

leet dot = document.getElementById()