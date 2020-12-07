
//  *'-.-'*'-.-'*'-.-'*-.-'*-.-'*-.-'*-.-'*'-.-'*'-.-'*'-.-'*
//         Project: Javascript
//  Assignment/Ver: Lab 1c
//          Author: Ron Mansolilli, ron.mansolilli@gmail.com
//            Date: 12-1-2020
//  *'-.-'*'-.-'*'-.-'*-.-'*-.-'*-.-'*-.-'*'-.-'*'-.-'*'-.-'*

// ----Instructions and notes--------------------------------

    /* Blackjack Advice (from Python Lab 19) */

// ----Global variables, arrays, etc. ------------------

// let hand = [];

// ----Functions----------------------------------------------

function sum() {
    let tally = 0;

    //Function to Sum array of numbers
    // let y1 = y.reduce((a, b) => a + b, 0);
    for (let i = 0; i < card.length; ++i) {
        // console.log(i)
        // console.log(card.length)
        tally += parseFloat(card[i].value);
        // tally += temp
        // console.log(tally);
        // tally += card[i].value;


    }
    
    // const array1 = y;
    // const reducer = (accumulator, currentValue) => accumulator + currentValue;
    // y1 = array1.reduce(reducer);
    // console.log(tally)
    return tally;
    };

// Utilized stackflow & MDA to research Reduce @ below:
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

// //Input
//     hand.push(prompt('First card (1-9, j, q, k, a):'));
//     hand.push(prompt('Second card (1-9, j, q, k, a):'));
//     hand.push(prompt('Third card (1-9, j, q, k, a):'));    
//     console.log(hand);

let card = document.getElementsByClassName("card");
let inputs = document.getElementById("inputs");
let bt2 = document.getElementById("bt2");
let bt1 = document.getElementById("bt1");
let add = 0;

bt2.addEventListener('click', function() {
    // console.log(card[0].value);
    let add = sum();
    console.log(add);
});


// // Assign value to J, Q, K, A
//     for (let x2 = 0; x2 < 3; ++x2) {
//         if (hand[x2] === ("j") || hand[x2] === ("q") || hand[x2] === ("k")) {
//             hand[x2] = 10;
//         } else if (hand[x2] === "a") {
//             hand[x2] = 11;
//         };
//     };

// // Str -> Int
//     for (let x3 = 0; x3 < 3; ++x3) {
//         hand[x3] = parseInt(hand[x3])
//     }

// /* Output */
//     let recommendation = hand_eval(hand);
//     // Send hand to evaluate function and rtn recommendation

//     alert(`Lab 19 \n ---------- 
//             \n Hand: ${sum(hand)} 
//             \n Recommendation: ${recommendation} 
//         `);

