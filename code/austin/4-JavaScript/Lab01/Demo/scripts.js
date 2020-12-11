
const container = document.getElementById('container')
const tipForm = document.getElementById('tipForm')

let percentage = 0
let count = 0

const total = document.createElement('input')
total.setAttribute('type', 'number')
total.setAttribute('placeholder', 'Enter a Total')
total.setAttribute('id', 'total')


const slider = document.createElement('input')
slider.setAttribute('type', 'range')
slider.setAttribute('id', 'slider')
slider.setAttribute('value', 0)

const percent = document.createElement('p')
container.insertBefore(total, tipForm)
tipForm.appendChild(slider)
tipForm.appendChild(percent)

tipForm.onchange = function(){
    percentage = slider.value
    percent.innerText = percentage + '%'
    console.log(percentage)
}

const submit = document.createElement('input')
submit.setAttribute('type', 'button')
submit.setAttribute('value', 'submit')
tipForm.appendChild(submit)

submit.onclick = function(){
    const checkVal = document.getElementById('finalTotal')
    const tip = parseInt(total.value * parseInt(percentage) / 100)
    console.log(tip)

    if (checkVal === null) {
        const finalTotal = document.createElement('p')
    
        finalTotal.setAttribute('id', 'finalTotal')
        finalTotal.innerText = 'Final bill: ' + tip
        
        total.value = ""
        percent.innerText = ""
        slider.value = 0
        container.appendChild(finalTotal)
    }   else {
        checkVal.innerText = 'Your tip is $' + tip
        total.value = ""
        percent.innerText = ""
        slider.value = 0
    }
}

