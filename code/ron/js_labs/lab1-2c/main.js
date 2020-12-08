
//  *'-.-'*'-.-'*'-.-'*-.-'*-.-'*-.-'*-.-'*'-.-'*'-.-'*'-.-'*
//         Project: Javascript
//  Assignment/Ver: Lab 2c
//          Author: Ron Mansolilli, ron.mansolilli@gmail.com
//            Date: 12-1-2020
//  *'-.-'*'-.-'*'-.-'*-.-'*-.-'*-.-'*-.-'*'-.-'*'-.-'*'-.-'*

// ----Instructions and notes--------------------------------

    /* Blackjack Advice (from Python Lab 19) */

// ----Global variables, arrays, etc. ------------------

    /* none */

// ----Functions----------------------------------------------

function check_jqka(cc) {
    //Check for Jack/Queen/King/Ace and change values appropriately
    // console.log("Made it to check jqka")
    // console.log(cc)
    if (cc === ("j") || cc === ("q") || cc === ("k")) {
        cc = 10;
        // console.log("needs a 10")
    } else if (cc === "a") {
        cc = 11;
    };
    // console.log(cc)
    return cc;
};

function sum() {
    //Function to Sum array of numbers
    let tally = 0;
    for (let i = 0; i < card.length; ++i) {
        // console.log(card[i].value)
        card[i].value = check_jqka(card[i].value);
        // console.log(card[i].value)
        tally += parseFloat(card[i].value);
    };
    return tally
};

function hand_eval(x1) {
    //Hand evaluation function
    if (x1 < 17) {
        return ('Hit');
    } else if (x1 > 16 && x1 < 21) {
        return ('Stay');
    } else if (x1 === 21) {
        return ('Blackjack!');
    } else if (x1 > 21) {
        return ('Busted');
    } else {
        return ('Invalid Selection');
    };
};

// ----Main Code---------------------------------------------

// Declarations

    let card = document.getElementsByClassName("card");
    let inputs = document.getElementById("inputs");
    let bt2 = document.getElementById("bt2");
    let bt1 = document.getElementById("bt1");
    let results = document.getElementById("results")
    let add = 0;

// Code

    bt2.addEventListener('click', function() {
        // Button
        console.log(card[0].value);
        add = sum();
        // console.log(add);
        let recommendation = hand_eval(add);
        results.innerText = recommendation;
        // console.log(recommendation);
    });

