// Lab25 ATM

transactions = []

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
        alert(transactions)
    };

};

let my_account = new Bank_Account();
let select = "";

// Account REPL

while (select != "done") {
    select = prompt("What would you like to do? Type 'deposit,' 'withdraw,' 'check balance,' 'history'  or 'done' ");

    if (select == "deposit") {
        amount = parseInt(prompt("Amount of deposit? "))
        my_account.deposit(amount)
    }
        
    else if (select == "withdraw") {
        amount = parseInt(prompt("Amount to withdraw? "))
        my_account.withdraw(amount)
    }
        
    else if (select == "check balance") {
        amount = parseInt(prompt("Amount you want to spend? "))
        my_account.check_withdrawal(amount)
    }

    else if (select == "history") {
        let history = my_account.print_transactions() 
    }

    else if (select == "done") {
        break
    }
    else {
        alert("Please type a valid selection")
    }    
}
    

