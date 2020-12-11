let result = document.getElementById('result');
let card1 = document.getElementById('card1');
let card2 = document.getElementById('card2');
let card3 = document.getElementById('card3');
let give_advice = document.getElementById('advice');
let total = 0;

let list = {
    A: '1', 2: '2', 3: '3', 4: '4',
    5: '5', 6: '6', 7: '7', 8: '8',
    9: '9', 10: '10', J: '10', Q: '10', K: '10'
};

function add(a, b, c) {
    return parseInt(a)+parseInt(b)+parseInt(c)
}

function addTotal(e) {
    total = add(list[card1.value], list[card2.value], list[card3.value])
    console.log(total);
    if (total < 17) {
        result.innerText = `Total: ${total} \n I advise you to Hit!`;
    } else if (17 <= total && total < 21) {
        result.innerText = `Total: ${total} \n I advise you to Stay!`;
    } else if (total == 21) {
        result.innerText = `Total: ${total} \n No advice needed. BlackJack!`;
    } else {
        result.innerText = `Total: ${total} \n :( Already Busted!`;
    }
};

give_advice.addEventListener('click', addTotal);

