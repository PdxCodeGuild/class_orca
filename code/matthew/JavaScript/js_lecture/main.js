// let p = document.getElementsByTagName("p");
// let red = document.getElementsByClassName("red");
// let title = document.getElementById("title");
// let blue = document.getElementsByClassName("blue");

// title.innerHTML = "<strong><em>Hello World!</em></strong>";

// for (let i=0; i<red.length; i++) {
//     red[i].innerText = "why is this text not red? We'll have to fix that...";
//     red[i].style.backgroundColor = "red";
//     red[i].style.color = "white";
//     red[i].style.border = "1px solid black";
// }

// let div = document.createElement("div");
// div.style.width = "400px"
// div.style.height = "400px"
// div.style.border = "2px dashed black"
// div.style.backgroundColor = "red";



// let img = document.createElement("img");
// img.src = "Cat.jpg";
// img.style.maxWidth = "100%";
// img.style.margin = "24px";


// div.appendChild(img);



// title.appendChild(div);

// div = document.getElementById("js");
// div.style.backgroundColor = "red";

// console.log(div);
// console.log(img);

// img.addEventListener('click', function(event) {
//     alert("Hello World!");
// });




let btn = document.getElementById("btn");
let more = document.getElementById("more");
// let num1 = document.getElementById("num1");
// let num2 = document.getElementById("num2");
let num3 = document.getElementById("num3");
let results = document.getElementById("results");
let inputs = document.getElementById("inputs");

let numCounter = 3;

// console.log(nums);

btn.addEventListener('click', function(e) {
    let li = document.createElement("li");
    let nums = document.getElementsByClassName("num");
    let sum = 0;
    for (let i=0; i<nums.length; i++) {
        if (nums[i].value) {
            sum += parseFloat(nums[i].value)    
        }
    }
    li.innerText = sum
    // console.log(nums)
    // li.innerText = `${nums[0].value} + ${nums[1].value} = ${parseFloat(nums[0].value) + parseFloat(nums[1].value)}` ;
    results.appendChild(li);
});

more.addEventListener('click', function(e) {
    let newInput = document.createElement("input");
    newInput.type = "number";
    newInput.placeholder = `Number ${numCounter}`;
    numCounter++;
    newInput.classList.add("num");
    inputs.append(" + ");
    inputs.appendChild(newInput);
});


