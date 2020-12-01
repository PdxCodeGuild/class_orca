let list = {
    A: '1', 2: '2', 3: '3', 4: '4',
    5: '5', 6: '6', 7: '7', 8: '8',
    9: '9', 10: '10', J: '10', Q: '10', K: '10'
};

let first_card = prompt('What is your first card?')
let second_card = prompt('What is your second card?')
let third_card = prompt('What is your third card?')


function add(a, b, c) {
    return parseInt(a)+parseInt(b)+parseInt(c)
}

let total = add(list[first_card], list[second_card], list[third_card])

if (total < 17) {
    alert(`Total: ${total}. Hit!`)
} else if (17 <= total && total < 21) {
    alert(`Total: ${total}. Stay!`)
} else if (total == 21) {
    alert(`Total: ${total}. BlackJack!`)
} else {
    alert(`Total: ${total}. Already Busted!`)
}