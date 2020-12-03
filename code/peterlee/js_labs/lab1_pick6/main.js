function random(min, max) {
    return Math.round(Math.random() * (max - min) + min);
}

function pick6() {
    let randomSet = [];
    for (let i=0; i < 6; i++) {
        randomSet.push(random(1, 99));
    }
    return randomSet;
}

function matches(a, b=winningTicket) {
    let matchCounter = 0;
    for (let i=0; i < 6; i++) {
        if (a[i] === b[i]) {
            matchCounter += 1;
        }
    }
    return matchCounter;
}

function winnings() {
    let numberOfTickets = document.getElementById('usertickets').value;
    let numTickets = parseInt(numberOfTickets);
    let currentBalance = 0;
    for (let i=0; i < numTickets; i++) {
        currentBalance -= 2;

        let ticket = pick6();
        let currentMatches = matches(ticket);

        if (currentMatches === 1) {
            currentBalance += 4;
        }
        else if (currentMatches === 2) {
            currentBalance += 7;
        }
        else if (currentMatches === 3) {
            currentBalance += 100;
        }
        else if (currentMatches === 4) {
            currentBalance += 50000;
        }
        else if (currentMatches === 5) {
            currentBalance += 1000000;
        }
        else if (currentMatches === 6) {
            currentBalance += 25000000;
        }
    }
    results.innerText =`${currentBalance}`;
    let expenses = 2*numTickets;
    let earnings = expenses + currentBalance;
    let roi = (earnings - expenses)/(expenses);
    results.innerText =`Your current balance is $${currentBalance}\n\nYour expenses are $${expenses}\n\nYour earnings are $${earnings} \n\nYour ROI is ${roi}`;
    return;
}

let winningTicket = pick6();


let btn = document.getElementById("btn");
let results = document.getElementById("results");

btn.addEventListener("click", winnings);


