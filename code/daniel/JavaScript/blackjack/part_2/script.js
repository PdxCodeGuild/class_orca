let body = document.getElementById("body");
let btn = document.getElementById("btn");
let points = document.getElementById("points");
let hit = document.getElementById("hit");
let stay = document.getElementById("stay");
let flop = document.getElementById("results");
let cards = document.getElementById("cards"); 
let deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J' ,'Q', 'K', 'A']; 
let standby_hand = [];
let play_again = document.getElementById("play_again");

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
    points.innerText = "you have "+value+".";
    results();
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
    let value = 0;
    for (let x=0; x<standby_hand.length; x++) {
        if (standby_hand[x] === 'A') {
            value ++;
        } else if (['J', 'Q', 'K'].includes(standby_hand[x])) {
            value += 10;
        } else {
            value += parseInt(standby_hand[x]);
        }};
    if (value > 21) {
        let advice = "You busted!";
        flop.innerText = advice;
        end_game()
    } else if (value === 21) {
        let advice = "Blackjack!";
        flop.innerText = advice;
        end_game()
    } else if (17 <= value < 21) {
        let advice = "You should stay.";
        flop.innerText = advice;
    } else if (value < 17) {
        let advice = "You should hit.";
        flop.innerText = advice;
    };
};

play_again.addEventListener('click', function() {
    location.reload()
})

function end_game() {
    play_again.style.display = 'block';
    
}