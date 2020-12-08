let card_value = {'A': '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10', 'J': '10', 'K': '10', 'Q': '10'};

// Change to input fields & add button
const inputs = document.querySelectorAll('input')

let new_array = [];
let sum = 0;

let cards = [];
// console.log(cards)

// let card1 = inputs[0].value;
// let card2 = inputs[1].value;
// let card3 = inputs[2].value;

let btn = document.getElementById("btn");
btn.addEventListener('click', function() {
    let card1 = inputs[0].value;
    let card2 = inputs[1].value;
    let card3 = inputs[2].value;
    cards.push(card1, card2, card3);
    console.log(cards)
    getValue(cards);
    
});


function getValue(cards) {
    for (let i = 0; i < cards.length; i++){
        for (var key in card_value) {
            if (key === cards[i]) {
                new_array.push(card_value[key])
                console.log(card_value[key])
            }
        }
    }
    console.log(new_array, "This is the value of cards") 
    addCards(new_array);
    return new_array
};

// getValue(cards)

function addCards(new_array) {
    for (let i = 0; i < new_array.length; i++) {
        new_array[i] = parseInt(new_array[i])
        sum += new_array[i] 
    }
    console.log(sum, "SUM")
    vegas_baby(sum);
};


//Change alerts to displays
const giveAdvice = document.getElementById('h4');

function vegas_baby(sum) {
    console.log(giveAdvice, "sum in advice")
    if (sum < 17) {
        giveAdvice.innerText = "Hit!"
    }

    if (sum >= 17 && sum < 21) {
        giveAdvice.innerText = "Stay"
    }

    if (sum == 21) {
        giveAdvice.innerText = "Blackjack!"
    }

    if (sum > 21) {
        giveAdvice.innerText = "Already busted"
    }
};






