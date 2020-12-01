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

let winningTicket = pick6();
let currentBalance = 0;

for (let i=0; i < 100000; i++) {
    let ticket = pick6();

    currentBalance -= 2;

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

alert(currentBalance);

let earnings = 200000 + currentBalance;
let roi = (earnings - 200000)/200000
alert(`Your earnings are ${earnings} \n\nYour ROI is ${roi}`);




