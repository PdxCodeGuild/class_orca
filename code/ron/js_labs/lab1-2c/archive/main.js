
//  *'-.-'*'-.-'*'-.-'*-.-'*-.-'*-.-'*-.-'*'-.-'*'-.-'*'-.-'*
//         Project: Javascript
//  Assignment/Ver: Lab 2c
//          Author: Ron Mansolilli, ron.mansolilli@gmail.com
//            Date: 12-4-2020
//  *'-.-'*'-.-'*'-.-'*-.-'*-.-'*-.-'*-.-'*'-.-'*'-.-'*'-.-'*

// ----Instructions and notes--------------------------------

    /* Blackjack Advice (from Python Lab 19) */

// ----Global variables, arrays, etc. ------------------

// let hand = []; 


// ----Functions----------------------------------------------

function hand_process(e) {
    // Assign value to J, Q, K, A

    // let inputs = document.getElementById("inputs");
    let card = document.getElementsByClassName("card")

    console.log("fn: hand process");
    console.log(`1. ${card}`);

    for (let x2 = 0; x2 < card.length; ++x2) {
        if (card[x2].value === ("j") || card[x2].value === ("q") || card[x2].value === ("k")) {
            card[x2].value = 10;
        } else if (card[x2] === "a") {
            card[x2] = 11;
        };

    console.log(`2. ${card}`);
    final = str_to_int(card);
    console.log(`4. ${final}`);
    hand_final = sum(final);
    results.innerText = hand_final;
    };
};

function str_to_int(hand) {
    //Function to convert str inputs to integers
    console.log(`3. Str-Int ${hand}`);
    for (let x3 = 0; x3 < 3; ++x3) {
        hand[x3].value = parseInt(hand[x3].value);
    return hand
    }
} 

function sum(y) {
    //Function to Sum array of numbers
    // let y1 = y.reduce((a, b) => a + b, 0);
    return y;
    // console.log(y1);
    };

//Utilized stackflow & MDA to research Reduce @ below:
//https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduce

function hand_eval(x) {
    //Hand evaluation function
    x1 = sum(x)
    if (x1 < 17) {
        return ('Hit');
    } else if (x1 > 16 && x < 21) {
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

//Input
    // hand.push(prompt('First card (1-9, j, q, k, a):'));
    // hand.push(prompt('First card (1-9, j, q, k, a):'));
    // hand.push(prompt('First card (1-9, j, q, k, a):'));    
    // console.log(hand);

    // let inputs = document.getElementById("inputs");
    let card = document.getElementById("card");
    let bt1_add = document.getElementById("bt1_add");
    let bt2_advice = document.getElementById("bt2_advice");

//Code

    bt2_advice.addEventListener('click', hand_process);
    //     console.log('the beginning')
    //     // console.log(inputs);
    //     console.log(`1. ${inputs}`);
    //     // hand_process();
    //     console.log(`2. ${inputs}`);
    // });


    // // Assign value to J, Q, K, A
    // for (let x2 = 0; x2 < 3; ++x2) {
    //     if (hand[x2] === ("j") || hand[x2] === ("q") || hand[x2] === ("k")) {
    //         hand[x2] = 10;
    //     } else if (hand[x2] === "a") {
    //         hand[x2] = 11;
    //     };
    // };

// Str -> Int


/* Output */
    // let recommendation = hand_eval(hand);
    // Send hand to evaluate function and rtn recommendation

    // alert(`Lab 19 \n ---------- 
    //         \n Hand: ${sum(hand)} 
    //         \n Recommendation: ${recommendation} 
    //     `);

