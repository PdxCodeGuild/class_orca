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
        if (cards[x] == 'A') {
            value ++;
        } else if (cards[x] in ['J', 'Q', 'K']) {
            value += 10;
        } else {
            value += cards[x];
        }}
    return value 
    }

function main() {
    let cards = hand();
    let points = point_value(cards);
    console.log(cards, points);
};

main();
