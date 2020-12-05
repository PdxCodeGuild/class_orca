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

