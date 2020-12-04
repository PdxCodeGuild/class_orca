


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
let num1 = document.getElementById("num1");
let num2 = document.getElementById("num2");
let results = document.getElementById("results");

btn.addEventListener('click', function(e) {
    let li = document.createElement("li");
    li.innerText = `${num1.value} + ${num2.value} = ${parseFloat(num1.value) + parseFloat(num2.value)}`;
    results.appendChild(li);
});



