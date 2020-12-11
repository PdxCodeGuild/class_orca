
let transactions = []
let balance = 0


let printTransactions = function(){
    // for each loop: if it was python: "for tans in transactions"
    // arrow => essentially means return
    transactions.forEach(trans => alert(trans))
}

let main = function () {
    let selectionInput = prompt("Hello, welcome to teh Evil Bank Corp ATM. Please selection from the following options: \n 1: Check your balance \n 2 : Deposit funds \n3 : Withdraw \n4 : History \n 5: Quit")

    if (selectionInput === '1'){
        console.log('you made it')
        prompt(`You have ${balance} available.`)
        main();
    }
    else if (selectionInput === '2'){
        let deposit = prompt("please enter the amount you wish to deposit ")
        balance +=  parseInt(deposit) 
        transactions.push(`you deposited ${deposit}`)
        main();
    }
    else if (selectionInput === '3'){
        let withdraw = prompt("please enter the amount you wish to withdraw ")
        balance -=  parseInt(withdraw)
        transactions.push(`you withdrew ${withdraw}`)
        main();
    }
    else if (selectionInput === '4'){
        printTransactions();
        main();
    }
    else if (selectionInput === '5'){
        prompt("Please remember to grab your card and possessions before leaving this machine. Have a good day!  @Evil Bank Corp")
        quit();
    }
}

main();
