
// let total = 0;
// let len = nums.length;
// let average = sum/len;
// let avg = average.toFixed(2);

document.body.style.display = 'flex';
document.body.style.alignItems = 'center';
document.body.style.flexDirection = 'column';
document.body.style.backgroundColor = 'lightblue';
document.body.style.color = "red";

var returnnum;

let inputs = document.getElementById('inputs');
inputs.style.width = "55%";
inputs.marginLeft = 'auto';
inputs.marginRight = 'auto';
let btns = document.getElementById('btns');
let moreBtn = document.getElementById('moreBtn');
let averageBtn = document.getElementById('averageBtn');
let result = document.getElementById('result');
let displayResult = document.getElementById('displayResult');
displayResult.style.fontSize = '40px';
displayResult.style.color = 'red';
let num = document.getElementsByClassName('num');


moreBtn.addEventListener('click', function() {
    inputs.append(" + ");
    let newNumber = document.createElement("input");
    newNumber.type = "number";
    newNumber.classList.add("num");
    inputs.appendChild(newNumber);
    
})


averageBtn.addEventListener('click', function(e) {
    var nums = [];
    var x = document.getElementsByClassName('num')
    for (let i=0; i < num.length; i++) {
        nums.push(parseInt(num[i].value))
        var sum = nums.reduce(function(a, b) {
            return a + b;
        }, 0);
        
    }
    console.log(nums)
    var total = 0
    let len = nums.length
    let average = sum/len;
    let avg = average.toFixed(2);
    displayResult.innerText = `Your average is ${avg}!`
    console.log(avg)
    
})
