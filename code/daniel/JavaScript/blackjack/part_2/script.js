let body = document.getElementById("body");
let btn = document.getElementById("btn");
let points = document.getElementById("points");
let hit = document.getElementById("hit");
let stay = document.getElementById("stay");
let cards = document.getElementById("cards"); 
let deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J' ,'Q', 'K', 'A']; 
let standby_hand = [];

btn.addEventListener('click', deal);
function deal() {
    for (let x=0; x<2; x++) {
        let card = document.createElement("p");
        card.id = "card";
        card.innerText = deck[Math.floor(Math.random() * deck.length)];
        standby_hand.push(card.innerText);
        cards.appendChild(card);
    };
    btn.remove();
    math();
}

function math(cards) {
    let value = 0;
    for (let x=0; x<standby_hand.length; x++) {
        if (standby_hand[x] === 'A') {
            value ++;
        } else if (['J', 'Q', 'K'].includes(standby_hand[x])) {
            value += 10;
        } else {
            value += parseInt(standby_hand[x]);
        }};
    console.log(value)
    points.innerText = "you have "+value+".";
};

hit.addEventListener('click', add_card);
function add_card() {
    let card = document.createElement("p");
    card.innerText = deck[Math.floor(Math.random() * deck.length)];
    standby_hand.push(card.innerText);
    cards.appendChild(card);
    math();
};

stay.addEventListener('click', results);
function results() {
    let points = getElementById("points");
    

}


// function crunch_points(points) {
//     if (points < 17) {
//         let advice = "You should hit.";
//         return advice;
//     } else if (17 <= points <= 21) {
//         let advice = "You should stay.";
//         return advice;
//     } else if (points === 20) {
//         let advice = "Blackjack!";
//         return advice;
//     } else if (points > 21) {
//         let advice = "You busted!";
//         return advice;
//     };
// };

// function main() {
//     let cards = hand();
//     // let points = point_value(cards);
//     // let advice = crunch_points(points);
//     // cards = cards.join(', ');
//     // alert('Your hand was a '+ cards + '.');
//     // alert("That's " + points + " points. "+ advice);
// };

// main();
