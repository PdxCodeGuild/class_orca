var deck = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J' ,'Q', 'K'];

function hand() {
    let hand = [];
    for (let x=0; x<2; x++) {
        hand.push(deck[Math.floor(Math.random() * deck.length)]);
    };
    return hand;
}

function point_value(cards) {
    let value = 0;
    for (let x=0; x<2; x++) {
        if (cards[x] === 'A') {
            value ++;
        } else if (['J', 'Q', 'K'].includes(cards[x])) {
            value += 10;
        } else {
            value += cards[x];
        }};
    return value;
    };

function crunch_points(points) {
    if (points < 17) {
        let advice = "You should hit.";
        return advice;
    } else if (17 <= points <= 21) {
        let advice = "You should stay.";
        return advice;
    } else if (points === 20) {
        let advice = "Blackjack!";
        return advice;
    } else if (points > 21) {
        let advice = "You busted!";
        return advice;
    };
};

function main() {
    let cards = hand();
    let points = point_value(cards);
    let advice = crunch_points(points);
    cards = cards.join(', ');
    alert('Your hand was a '+ cards + '.');
    alert("That's " + points + " points. "+ advice);
};

main();
