function cardValue(a) {
    if (a === 'J' || a === 'j'|| a === 'Q' || a === 'q'|| a === 'K' || a === 'k') {
        return 10;
    }
    else if (a === 'A' || a === 'a') {
        return 1;
    }
    else {
        return parseInt(a);
    }
}

let btn = document.getElementById('btn');
let more = document.getElementById("more");
let cardsDiv = document.getElementById('cardsdiv');
let cardCounter = 2;

more.addEventListener('click', function(e) {
    let newCard = document.createElement("input");
    newCard.type = "text";
    newCard.placeholder = `Card ${cardCounter}`;
    cardCounter++;
    newCard.classList.add("cards");
    
    cardsDiv.append(" + ");
    cardsDiv.appendChild(newCard);
});


btn.addEventListener('click', function(e) {
    let results = document.getElementById('results');
    let cards = document.getElementsByClassName('cards');
    let hand = 0;
    let advice;

    for (let i = 0; i < cards.length; i++) {
        if (cards[i].value) {
        hand += cardValue(cards[i].value);
        }
    }
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
    results.innerText = `Your hand is ${hand}\n${advice}`;
});