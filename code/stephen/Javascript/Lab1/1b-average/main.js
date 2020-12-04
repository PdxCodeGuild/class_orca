var nums = [];
let total = 0;
let len = nums.length;
// let average = sum/len;
// let avg = average.toFixed(2);

function getSum(e) {

}
var returnnum;

let inputs = document.getElementById('inputs');
let btns = document.getElementById('btns');
let moreBtn = document.getElementById('moreBtn');
let averageBtn = document.getElementById('averageBtn');
let result = document.getElementById('result');
let displayResult = document.getElementById('displayResult');
// let num = document.getElementsByClassName('num');


moreBtn.addEventListener('click', function() {
    inputs.append(" + ");
    let newNumber = document.createElement("input");
    newNumber.type = "number";
    newNumber.classList.add("num");
    inputs.appendChild(newNumber);
})

averageBtn.addEventListener('click', function() {
    let num = document.getElementsByClassName('num');
    returnnum = num.value;
    nums.push(returnnum);
    console.log(nums);
})