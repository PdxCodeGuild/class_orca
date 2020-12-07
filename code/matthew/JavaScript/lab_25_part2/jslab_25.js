let transactions = []
let balance = 19.47

// Deposit 
let depositInput = document.getElementById("depositInput")
let btn = document.getElementById("btn")

// Withdraw
let withdrawInput = document.getElementById("withdrawInput")
let withdrawBtn = document.getElementById("withdrawBtn")

// Balance display
let balanceDisplay = document.getElementById("balanceDisplay")

// History display
let history = document.getElementById('history')

btn.addEventListener('click', function() {
        // Deposit balance section
        balance += parseInt(depositInput.value)
        // following line communicated with line: displayText.id = 'displayText'
        let checkValueDeopsit = document.getElementById('displayText')
        checkValueDeopsit.innerText = balance

        // Deposite History update section
        let historyText = document.createElement('p')
        historyText.innerText = `You withdrew $${depositInput.value} leaving a balance of $${balance}`
        history.appendChild(historyText)  
})

withdrawBtn.addEventListener('click', function() {
        // withdraw balance section
        balance -= parseFloat(withdrawInput.value)

        // following line communicated with line: displayText.id = 'displayText'
        let checkValueWithdraw = document.getElementById('displayText')
        checkValueWithdraw.innerText = balance

        // Withdraw History update section
        let historyText = document.createElement('p')
        historyText.innerText = `You withdrew $${withdrawInput.value} leaving a balance of $${balance}`
        history.appendChild(historyText)  
})

// creates the p tag to be displayed
let displayText = document.createElement('p')

// comminucates with line to get data out of function : let checkValueDeopsit = document.getElementById('displayText')  
displayText.id = 'displayText'
// displayText.setAttribute('id','displayText')          shorthand for previous line
// innerText is how JavaScript adds it in

// withdraw version
displayText.id = 'displayText'

displayText.innerText = balance
balanceDisplay.appendChild(displayText)





