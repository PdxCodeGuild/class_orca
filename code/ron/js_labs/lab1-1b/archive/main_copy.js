
//  *'-.-'*'-.-'*'-.-'*-.-'*-.-'*-.-'*-.-'*'-.-'*'-.-'*'-.-'*
//         Project: Javascript
//  Assignment/Ver: Lab 1b
//          Author: Ron Mansolilli, ron.mansolilli@gmail.com
//            Date: 12-1-2020
//  *'-.-'*'-.-'*'-.-'*-.-'*-.-'*-.-'*-.-'*'-.-'*'-.-'*'-.-'*

// ----Instructions and notes--------------------------------

/* Pick 6 (from Python Lab 14) */

// ----Global variables, lists, dictionaries------------------

let matches = 0
let money_spent = 0
let prize_money = 0
let winning_ticket = 0

// ----Functions----------------------------------------------

function random_ticket_nums() {
    //Random ticket generator
    let x = 1;
    let ticket = [];
    let c1 = 0;
    while (c1 <= 6) {
        // randomizer (but not including 1)
        ticket.push(Math.floor(Math.random()*10));
        c1++;
    };
    return ticket;
};

function num_match(matches) {
    //Checking # matches, assigning price money
    let prize = 0;

    if (matches === 1) {
        prize += 2;
    }
    if (matches === 2) {
        prize += 7;
    }
    if (matches === 3) {
        prize += 100;
    }   
    if (matches === 4) {
        prize += 50000;
    }
    if (matches === 5) {
        prize += 1000000;
    }   
    if (matches === 6) {
        prize += 2500000;
    }
    return prize;
}


// ----Main Code---------------------------------------------

for (let x1 = 1; x1 <= 10000; x1++) {
    //Building tickets, setting paramters
    let my_ticket = random_ticket_nums();
    let winning_ticket = random_ticket_nums();
    matches = 0;
    money_spent += 2;

    for (let x2 = 0; x2 <= 5; x2++) {
        //Checking tickets for matches and tallying prizes
        if (my_ticket[x2] === winning_ticket[x2]) {
            matches += 1;
            if (matches > 0) {
                prize_money += num_match(matches);
                winning_ticket += 1;
            };
        };
    };
};

/* Output */

let roi = (((prize_money - money_spent)/money_spent)*100);

alert(`Lab 14 \n ---------- 
        \n Investment: ${money_spent} 
        \n Investment: ${winning_ticket} 
        \n Prize Money: ${prize_money}
        \n Net Income: ${prize_money - money_spent}
        \n ROI: ${roi = roi.toFixed(2)}%

        `);

