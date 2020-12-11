let num1 = document.getElementById('num1');
let num2 = document.getElementById('num2');
let operator = document.getElementById('operator');
let answer = document.getElementById('answer');
let solve = document.getElementById('solve');

solve.addEventListener('click', function(){
    if (operator.value === 'add') {
        answer.innerText = parseFloat(num1.value) + parseFloat(num2.value);
    } else if (operator.value === 'subtract') {
        answer.innerText = parseFloat(num1.value) - parseFloat(num2.value);
    } else if (operator.value === 'multiply') {
        answer.innerText = parseFloat(num1.value) * parseFloat(num2.value);
    } else if (operator.value === 'divide') {
        answer.innerText = parseFloat(num1.value) / parseFloat(num2.value);
    }
});
