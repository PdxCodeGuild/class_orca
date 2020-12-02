let card_value = {'A': '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10', 'J': '10', 'K': '10', 'Q': '10'};


let card1 = prompt("Please enter your first card ");
let card2 = prompt("Please enter your second card ");
let card3 = prompt("Please enter your third card ");

let cards = [card1, card2, card3];
let new_array = [];
let sum = 0;

function getValue(cards) {
    for (let i = 0; i < cards.length; i++){
        for (var key in card_value) {
            if (key == cards[i]) {
                new_array.push(card_value[key])
                console.log(card_value[key])
            }
        }
        console.log(new_array)
    }
    return new_array
};

getValue(cards)

function addCards(new_array) {
    for (let i = 0; i < new_array.length; i++) {
        new_array[i] = parseInt(new_array[i])
        sum += new_array[i] 
    }
    console.log(sum)
    return sum
};

addCards(new_array)

function vegas_baby(sum) {
    if (sum < 17) {
        alert("Hit")
    }

    if (sum >= 17 && sum < 21) {
        alert("Stay")
    }

    if (sum == 21) {
        alert("Blackjack!")
    }

    if (sum > 21) {
        alert("Already busted")
    }
};

vegas_baby(sum)





