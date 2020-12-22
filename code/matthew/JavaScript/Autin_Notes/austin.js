// get attributes from the html
const container = document.getElementById('container')
const tipForm = document.getElementById('tipForm')

// set some constants
let percentage = 0
let count = 0

// create an input box and set attributes on following lines
const total = document.createElement('input')
// make the up and down part of the field
total.setAttribute('type', 'number')
// the text that is in the input
total.setAttribute('placeholder', 'Enter a Total')
total.setAttribute('id', 'total')

// creates a slider bar
const slider = document.createElement('input')
slider.setAttribute('type', 'range')
slider.setAttribute('id', 'slider')
slider.setAttribute('value', 0)

const percent = document.createElement('p')

container.insertBefore(total, tipForm)
tipForm.appendChild(slider)
tipForm.appendChild(percent)

// make an onchange function to get the sliders value
tipForm.oninput = function () {
    percentage = slider.value
    percent.innerText = percentage + '%'
    // console.log(percentage)
    } 

// create a button to submit our input
const submit = document.createElement('input')
submit.setAttribute('type', 'button')
submit.setAttribute('value', 'Submit')
tipForm.appendChild(submit)

// create a function that gets the value and does math
submit.onclick = function () {
    const checkVal = document.getElementById('finalTotal')
    const tip = (parseInt(total.value) * parseInt(percentage) / 100)

    if (checkVal === null) {
        const finalTotal = document.createElement('p')

        //do something
        finalTotal.setAttribute('id', 'finalTotal')
        finalTotal.innerText = 'your tip bill is $ ' + tip
        container.appendChild(finalTotal)

        // set the values back to null so the form reads nice
        total.value = ''
        percent.innerText = ''
        slider.value = 0
        container.appendChild(finalTotal)
    }
    else {
        checkVal.innerText = 'Your tip is $' + tip

        // set the values back to null so the form read nice
        total.value = ''
        percent.innerText = ''
        slider.value = 0
    }

    }


