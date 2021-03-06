function pick6(){
    let ticket = [];
    for (let i = 0; i<6; i++) {
        ticket.push(Math.round(100*Math.random()))
    };
    return ticket;
}


function compare_tickets(winningTicket, playerTicket) {
    let match = 0;
    for (let i=0; i<6; i++) {
        if (winningTicket[i] === playerTicket[i]) {
            match += 1;
        };

    };
    return match;
};


let winTick = document.getElementById('winTick');
let winTickDiv = document.getElementById('winTickDiv');
let playerTickDiv = document.getElementById('playerTickDiv');
let playerTick = document.getElementById('playerTick');
let playerTickBtn = document.getElementById('playerTickBtn')
let body = document.getElementsByTagName('body');

document.body.style.backgroundImage = "url('lottery-background.jpg')";
document.body.style.backgroundRepeat = "no-repeat";
document.body.style.backgroundSize = "cover";
document.body.style.textAlign = "center";
document.body.style.display = "flex";
document.body.style.flexDirection = "column";
document.body.style.justifyContent = "center";
buyTickets.style.width = "20%";
buyTickets.style.marginLeft = "auto";
buyTickets.style.marginRight = "auto";
document.body.style.fontSize = "24px";

winTickDiv.appendChild(winTick);




buyTickets.addEventListener('click', function() {
    var plays = parseInt(prompt('How many tickets would you like to buy?'));
    alert(`Hand over $${plays * 2}!`);
    let winningTicket = pick6();
    winTick.innerText= `The winning ticket is: ${winningTicket}`;
    let balance = (plays * -2);
    let earnings = 0;
    console.log(balance);
    var playerTick = document.createElement("button");
    playerTick.innerHTML = "Let's see if we got any winners!";
    playerTickBtn.appendChild(playerTick);
    playerTick.addEventListener('click', function() {
        for (i=0; i < plays; i++) {
            let playerTicket = pick6();
            // console.log(playerTicket);
            var matches = compare_tickets(winningTicket, playerTicket);
            playerTickP.innerText+= `Ticket ${i+1}: ${playerTicket} - Matches: ${matches}\n`;
            console.log(matches)
            if (matches === 1) {
                balance += 4;
                earnings += 4;
            } else if (matches === 2) {
                balance += 7;
                earnings +=7;
            } else if (matches === 3) {
                balance += 100;
                earnings += 100;
            } else if (matches === 4) {
                balance += 50000;
                earnings += 50000;
            } else if (matches === 5) {
                balance += 1000000;
                earnings += 1000000;
            } else if (matches === 6) {
                balance += 25000000;
                earnings += 25000000;
            }
        };
        alert(`After buying ${plays} tickets, your balance is $${balance}.  Your earnings are $${earnings}.  Better luck next time!`)
    })
});
 

// let winner = pick6();
// console.log(winner)
// let balance = 0;
// let earnings = 0;
// let plays = 1000;
// let cost = plays * 2


// for (let i = 0; i < plays; i++) {
//     balance -= 2;
//     let player = pick6();
//     let matches = compare_tickets(winner, player);
//     console.log(matches)
//     if (matches === 1) {
//         balance += 4;
//         earnings += 4;
//     } else if (matches === 2) {
//         balance += 7;
//         earnings +=7;
//     } else if (matches === 3) {
//         balance += 100;
//         earnings += 100;
//     } else if (matches === 4) {
//         balance += 50000;
//         earnings += 50000;
//     } else if (matches === 5) {
//         balance += 1000000;
//         earnings += 1000000;
//     } else if (matches === 6) {
//         balance += 25000000;
//         earnings += 25000000;
//     }
// }

// alert(`After 100,000 plays, your balance is $${balance}`)