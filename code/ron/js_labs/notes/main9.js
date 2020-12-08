
// get attributes from the HTML
const container = document.getElementById('container');
const tipForm = document.getElementById('tipForm');

// set some constants
let percentage = 0;
let count = 0; 

//create an input box and set attibutes
const total = document.createElement('input'); 
total.setAttribute('type', 'number');
total.setAttribute('placeholder', 'Enter a Total:');
total.setAttribute('id', 'total');

// create a slider bar
const slider = document.createElement('input');
slider.setAttribute('type', 'range');
slider.setAttribute('id', 'slider');
slider.setAttribute('value', 0);

const percent = document.createElement('p');

//output
container.insertBefore(total, tipForm);
tipForm.appendChild(slider);
tipForm.appendChild(total);

// make an onchange function to get the sliders value
tipForm.onchange = function() {
    percentage = slider.value;
    percent.innerText = percentage + '%'
    console.log(slider.value);
};

// create button to submit our input
const submit = document.createElement('input');
submit.setAttribute('type', 'button');
submit.setAttribute('value', 'Submit');
tipForm.appendChild(submit);

//create a function that gets the value and does math
submit.onclick = function () {
    const checkVal = document.getElementById('finalTotal');
    // const check = percent;
    // console.log(typeof(perent), 'this is the check');
    const tip = (parseInt(total.value) * percentage / 100);
    console.log(tip);

    if (checkVal === null) {
        const finalTotal = document.createElement('p');

        finalTotal.setAttribute('id', 'finalTotal');
        finalTotal.innerText = 'Your final bill is ' + tip;
        container.appendChild(finalTotal);

        total.value = '';
        percent.innerText = '';
        slider.value = 0;
        container.appendChild(finalTotal); 
    } else {
        checkVal.innerText = 'our tip is $' + tip;
        total.value = '';
        percent.innerText = '';
        slider.value = 0;
        
    };
};








