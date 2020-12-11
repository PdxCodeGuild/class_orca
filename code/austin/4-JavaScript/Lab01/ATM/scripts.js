// Lab25 ATM

transactions = []
let amount = 0

class Bank_Account {

    constructor(balance=0) {
        this.balance = balance;
        this.transactions = [];
    };

    check_balance() {
        console.log(this.balance)
        return this.balance
    };

    deposit(amount) {
        this.balance = this.balance + amount
        console.log(`Current balance: ${this.balance}`)
        transactions.push(`user deposited ${amount}`)
        return this.balance;
    };
    
    check_withdrawal(amount) {
        if (this.balance - amount >= 0) {
            let remaining = this.balance - amount
            alert(`Your balance would be ${remaining}`)
            return true;
        }
        else {
            return false;
            alert(`You don't have enough money`)
        }
    };
    
    withdraw(amount) {
        this.balance = this.balance - amount
        console.log(this.balance)
        transactions.push(`user withdrew ${amount}`)
        return this.balance
    };
    
    print_transactions() {
        console.log(transactions)
    };

};

let my_account = new Bank_Account();
let select = "";

// Account REPL

let dep = document.getElementById("deposit-radio")
let draw = document.getElementById("withdraw-radio")
let bal = document.getElementById("balance-radio")
let all = document.getElementById("history")
let btn = document.getElementById("btn");
let amountField = document.getElementById('amount-field')
let amountField2 = document.getElementById('amount-field2')

btn.addEventListener('click', function(){
    if (dep.checked = true) {
        my_account.deposit(parseInt(amountField.value))
        let display = document.getElementById("display")
        display.innerText = amountField.value
    }

    else if (draw.checked = true) {
        my_account.withdraw(parseInt(amountField2.value))
        let display = document.getElementById("display")
        display.innerText = amountField2.value
    }

    else if (bal.checked = true) {
        my_account.check_balance()
        let display = document.getElementById("display")
        display.innerText = balance
    }

    console.log(transactions)
});


