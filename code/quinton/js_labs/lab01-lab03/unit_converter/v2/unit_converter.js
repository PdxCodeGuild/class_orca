let feet = document.getElementById('feet');
let meters = document.getElementById('meters');
let miles = document.getElementById('miles');
let kilometers = document.getElementById('kilometers');
let yards = document.getElementById('yards');
let inches = document.getElementById('inches');

let converted_feet = document.getElementById('converted_feet');
let converted_meters = document.getElementById('converted_meters');
let converted_miles = document.getElementById('converted_miles');
let converted_kilometers = document.getElementById('converted_kilometers');
let converted_yards = document.getElementById('converted_yards');
let converted_inches = document.getElementById('converted_inches');

let user_input = document.getElementById('user_input');
let convert = document.getElementById('convert');
let units_converted = document.getElementById('units_converted');
let operator = document.getElementById('operator');
let converted_operator = document.getElementById('converted_operator');


let first_answer = 0;
let final_answer = 0;

convert.addEventListener('click', function() {
    if (operator.value === 'ft') {
        first_answer += parseFloat(user_input.value) * .3048
    } else if (operator.value === 'm') {
        first_answer += parseFloat(user_input.value)
    } else if (operator.value === 'mi') {
        first_answer += parseFloat(user_input.value) * 1609.34
    } else if (operator.value === 'km') {
        first_answer += parseFloat(user_input.value) * 1000
    } else if (operator.value === 'yd') {
        first_answer += parseFloat(user_input.value) * .9144
    } else if (operator.value === 'in') {
        first_answer += parseFloat(user_input.value) * .0254
    }

    if (converted_operator.value === 'mi') {
        final_answer += first_answer / 1609.34
    } else if (converted_operator.value === 'km') {
        final_answer += first_answer / 1000
    } else if (converted_operator.value === 'm') {
        final_answer += first_answer
    } else if (converted_operator.value === 'ft') {
        final_answer += first_answer / .3048
    } else if (converted_operator.value === 'yd') {
        final_answer += first_answer / .9144
    } else if (converted_operator.value === 'in') {
        final_answer += first_answer / .0254
    }
    units_converted.innerText = `${user_input.value}${operator.value} is ${final_answer}${converted_operator.value}`
})