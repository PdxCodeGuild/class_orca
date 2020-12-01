class ATM {
    constructor(balance=0) {
      this.balance = balance;
      this.transactions = [];
    }

    getBalance() {
      return this.balance;
    }

    deposit(depositAmount) {
        this.balance += depositAmount;
        this.transactions.push(`User deposited ${depositAmount}`);
        return;
    }

    checkWithdrawal(amount) {
        return this.balance > amount;
    }

    withdraw(withdrawAmount) {
        if (this.checkWithdrawal(withdrawAmount) === true) {
            this.balance -= withdrawAmount;
            this.transactions.push(`User withdrew ${withdrawAmount}`);
        }
        else {
            alert("Your balance is too low.");
            return;
        }
    }

    printTransactions() {
        return this.transactions.join("\n");
    }
}

let atm = new ATM();
while (true) {
    let option = prompt("What would you like to do ([d]eposit, [w]ithdraw, [c]heck balance, [h]istory, or [q]uit)?");

    if (option === "quit" || option === "q") {
        break;
    } 
    else if (option === "deposit" || option === "d") {
        let depositAmount =  parseFloat(prompt("How much would you like to deposit?"));
        atm.deposit(depositAmount);
    }
    else if (option === "withdraw" || option === "w") {
        let withdrawAmount = parseFloat(prompt("How much would you like to deposit?"));
        atm.withdraw(withdrawAmount);
    }
    else if (option === "check balance" || option === "c") {
        let balance = atm.getBalance();
        alert(balance);
    }
    else if (option === "history" || option === "h") {
        let history = atm.printTransactions();
        alert(history);
    }
}