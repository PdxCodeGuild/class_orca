
//  *'-.-'*'-.-'*'-.-'*-.-'*-.-'*-.-'*-.-'*'-.-'*'-.-'*'-.-'*
//         Project: Javascript
//  Assignment/Ver: Lab 1b
//          Author: Ron Mansolilli, ron.mansolilli@gmail.com
//            Date: 12-4-2020
//  *'-.-'*'-.-'*'-.-'*-.-'*-.-'*-.-'*-.-'*'-.-'*'-.-'*'-.-'*

// ----Instructions and notes--------------------------------

/* Pick 6 (from Python Lab 14) */ 

// ----Global variables, arrays, etc. ------------------

let matches = 0
let money_spent = 0
let prize_money = 0
let winners = 0

// ----Functions----------------------------------------------

function random_ticket_nums() {
    //Random ticket generator
    let ticket = [];
    let c1 = 0;
    while (c1 <= 5) {
        ticket.push(Math.floor(Math.random()*100));
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

//Declarations

    let my_ticket = []
    let bt1 = document.getElementById('bt1');
    let user_ticket = document.getElementById('user_ticket');
    let results = document.getElementById('results');

//Fuctions and Buttons

    bt1.addEventListener('click', function(event) {
        //'bt1' Generate user's ticket button (bt1)
        my_ticket = [];
        my_ticket = random_ticket_nums();
        user_ticket.innerText = my_ticket;
    });

    bt2.addEventListener('click', function(event) {
        //'bt2' Generate winning tickets and evaluate against user ticket
        money_spent = 0;    // Set initial state
        winners = 0;        // Set initial state
        prize_money = 0;    // Set initial state

        for (let x1 = 1; x1 <= 10000; ++x1) {
            //Building tickets, setting parameters
            let winning_ticket = random_ticket_nums();
            matches = 0;        // Reset
            money_spent += 2;
            for (let x2 = 0; x2 <= 5; ++x2) {
                //Checking tickets for matches and tallying matches
                for (let x3 = 0; x3 <= 5; ++x3) {
                    //Checking user numbers against each ticket number
                    if (my_ticket[x2] === winning_ticket[x3]) {
                        matches += 1;
                    };
                };
            };
            if (matches > 0) {
                //Tallying winning ticket earnings
                prize_money += num_match(matches);
                winners += 1; //Count total winning tickets
            };
        };

    //Output

    let roi = (((prize_money - money_spent)/money_spent)*100);
    results.innerText = `Investment: ${money_spent}
                        # of winning tickets: ${winners}
                        Prize Money: ${prize_money}
                        ROI: ${roi = roi.toFixed(2)}%`;
    });


