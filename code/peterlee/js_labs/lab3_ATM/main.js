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

let createBtn = document.getElementById("createbtn");
let resultsDiv = document.getElementById("resultsdiv");
let depositDiv = document.getElementById("depositdiv");
let withdrawDiv = document.getElementById("withdrawdiv");


createBtn.addEventListener('click', function() {
    //Create atm object
    var atm1 = new ATM();
    //remove start button
    createBtn.remove();
    //add balance section
    let balanceTitle = document.createElement("H1");
    balanceTitle.setAttribute("id", "balancetitle");
    balanceTitle.innerText = "Balance";
    let balanceP = document.createElement("p");
    balanceP.setAttribute("id", "balancediv");
    balanceP.innerText = atm1.balance;
    resultsDiv.appendChild(balanceTitle);
    resultsDiv.appendChild(balanceP);
    //add transaction section
    let transactionTitle = document.createElement("H1");
    transactionTitle.setAttribute("id", "transactiontitle");
    transactionTitle.innerText = "Transaction History";
    let transactionUL = document.createElement("UL");
    transactionUL.setAttribute("id", "transactionul");
    resultsDiv.appendChild(transactionTitle);
    resultsDiv.appendChild(transactionUL);
    //add deposit section
    let depositField = document.createElement("INPUT");
    depositField.setAttribute("id", "depositfield");
    depositField.setAttribute("type", "value");
    depositField.setAttribute("placeholder", "Deposit Amount");
    let depositBtn = document.createElement("BUTTON");
    depositBtn.setAttribute("id", "depositbtn");
    depositBtn.innerText = "Deposit";
    depositDiv.appendChild(depositField);
    depositDiv.appendChild(depositBtn);
    //add withdraw section
    let withdrawField = document.createElement("INPUT");
    withdrawField.setAttribute("id", "withdrawfield");
    withdrawField.setAttribute("type", "text");
    withdrawField.setAttribute("placeholder", "Withdrawal Amount");
    let withdrawBtn = document.createElement("BUTTON");
    withdrawBtn.setAttribute("id", "withdrawbtn");
    withdrawBtn.innerText = "Withdraw";
    withdrawDiv.appendChild(withdrawField);
    withdrawDiv.appendChild(withdrawBtn);

});

let depositBtn = document.getElementById("depositbtn");

depositBtn.addEventListener('click', function() {
    let balanceDiv = document.getElementById("balancediv");
    let tempDepositAmount = getElementById("depositfield");
    atm1.deposit(tempDepositAmount.value);
    balanceDiv.innerText = atm1.balance();
    tempDepositAmount.value = "";


});


