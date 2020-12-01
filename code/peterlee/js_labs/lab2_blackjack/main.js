alert("The card choices are: A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, or K");
let card1 = prompt("What is your first card?");
let card2 = prompt("What is your second card?");
let card3 = prompt("What is your third card?");

function cardValue(a) {
    if (a === 'J' || a === 'Q' || a === 'K') {
        return 10;
    }
    else if (a === 'A') {
        return 1;
    }
    else {
        return parseInt(a);
    }
}

let hand = cardValue(card1) + cardValue(card2) + cardValue(card3);

let advice;

if (hand < 17) {
    advice = "Hit";
}
else if (hand >= 17 && hand < 21) {
    advice = "Stay";
}
else if (hand === 21) {
    advice = "Blackjack!";
}
else {
    advice = "Already Busted";
}

alert(`${hand} ${advice}`);