// get attributes from the html
const container = document.getElementById('container')
const tipForm = document.getElementById('tipForm')

// set some constants
let percentage = 0

// create a input box and set attributes
const total = document.createElement('input')
total.setAttribute('type', 'number')
total.setAttribute('placeholder', 'Enter a Total')
total.setAttribute('id', 'total')

// crate a slider bar
const slider = document.createElement('input')
slider.setAttribute('type', 'range')
slider.setAttribute('id', 'slider')
slider.setAttribute('value', 0)

const percent = document.createElement('p')

container.insertBefore(total, tipForm)
tipForm.appendChild(slider)
tipForm.appendChild(percent)

// make a onchange function to get the sliders value on change
// or use on input to get it instantly
tipForm.oninput = function () {
  percentage = slider.value
  percent.innerText = percentage + '%'
  console.log(percentage)
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

    finalTotal.setAttribute('id', 'finalTotal')
    finalTotal.innerText = 'Your tip is $' + tip

    // set the values back to null so the form reads nice
    total.value = ''
    percent.innerText = ''
    slider.value = 0
    container.appendChild(finalTotal)
  } else {
    checkVal.innerText = 'Your tip is $' + tip

    // set the values back to null so the form reads nice
    total.value = ''
    percent.innerText = ''
    slider.value = 0
  }
}
