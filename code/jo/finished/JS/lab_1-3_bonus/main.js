let num = document.getElementById('num')
let deposit = document.getElementById('deposit')
let withrawl = document.getElementById('withrawl')
let transactions = document.getElementById('transactions')
let total = 0

function addMoney(e) {
    total += (+num.value)
    let li = document.createElement('li')
    li.innerText = (`You deposited $${num.value}. Your total balance is ${total}.`)
    transactions.appendChild(li)
    num.value = ''
}

function takeMoney(e) {
    total -= (+num.value)
    let li = document.createElement('li')
    li.innerText = (`You withdrew $${num.value}. Your total balance is ${total}.`)
    transactions.appendChild(li)
    num.value = ''
}

deposit.addEventListener('click', addMoney)

withdrawl.addEventListener('click', takeMoney)