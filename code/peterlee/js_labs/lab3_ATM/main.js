class ATM {
    constructor(balance=0) {
      this.balance = balance;
    }

    getBalance() {
      return this.balance;
    }

    deposit(depositAmount) {
        this.balance += parseDouble(depositAmount);
    }

    checkWithdrawal(amount) {
        return this.balance >= amount;
    }

    withdraw(withdrawAmount) {
        if (this.checkWithdrawal(parseDouble(withdrawAmount)) === true) {
            this.balance -= parseDouble(withdrawAmount);
        }
        else {
            alert("Your balance is too low.");
            return;
        }
    }
}

let createBtn = document.getElementById("createbtn");
let balanceDiv = document.getElementById("balancediv");
let depositDiv = document.getElementById("depositdiv");
let withdrawDiv = document.getElementById("withdrawdiv");
let transactionDiv = document.getElementById("transactiondiv");
let transactionUL = document.getElementById("transactionul");
let balanceDisplay = document.getElementById("balancep");
let inputField = document.getElementById("inputfield");

//Create atm object
var atm1 = new ATM();

createBtn.addEventListener('click', function() {
    //remove start button
    createBtn.remove();
    //add balance title
    let balanceTitle = document.createElement("H1");
    balanceTitle.setAttribute("id", "balancetitle");
    balanceTitle.innerText = "Balance";
    balanceDiv.insertBefore(balanceTitle, balanceDiv.children[0]);
    balanceDisplay.innerText = atm1.balance;
    //add transaction section
    let transactionTitle = document.createElement("H1");
    transactionTitle.setAttribute("id", "transactiontitle");
    transactionTitle.innerText = "Transaction History";
    transactionDiv.insertBefore(transactionTitle, transactionDiv.children[0]);
    //add deposit button
    let depositBtn = document.createElement("BUTTON");
    depositBtn.setAttribute("id", "depositbtn");
    depositBtn.innerText = "Deposit";
    depositDiv.appendChild(depositBtn);
    //add withdraw button
    let withdrawBtn = document.createElement("BUTTON");
    withdrawBtn.setAttribute("id", "withdrawbtn");
    withdrawBtn.innerText = "Withdraw";
    withdrawDiv.appendChild(withdrawBtn);

});
document.addEventListener('click', function(e) {
    if (e.target.id=="depositbtn") {
        atm1.deposit(inputField.value);
        balanceDisplay.innerText = atm1.balance;
        let transactionLi = document.createElement("LI");
        transactionLi.innerText = `Deposited ${inputField.value}`
        transactionUL.appendChild(transactionLi);
        inputField.value = "";
    }
    else if (e.target.id=="withdrawbtn") {
        atm1.withdraw(inputField.value);
        balanceDisplay.innerText = atm1.balance;
        if (atm1.checkWithdrawal(inputField.value)) {
        let transactionLi = document.createElement("LI");
        transactionLi.innerText = `Withdrew ${inputField.value}`
        transactionUL.appendChild(transactionLi);
        inputField.value = "";
        }
    }
});


