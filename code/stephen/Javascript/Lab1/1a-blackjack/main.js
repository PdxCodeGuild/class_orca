// cards = {
//     'A': 1,
//     'K': 10,
//     'Q': 10,
//     'J': 10,
// }

let cards = {
    'A': 1,     
    'K': 10,
    'Q': 10,
    'J': 10,
}
// card1 = input('What is your first card?\n>').upper()
// card2 = input('What is your second card?\n>').upper()
// card3 = input('What is your third card?\n>').upper()
let card1 = prompt('What is your first card?').toUpperCase()
let card2 = prompt('What is your second card?').toUpperCase()
let card3 = prompt('What is your third card?').toUpperCase()

// console.log(card1)

// if card1 in cards:
//     card1 = int(cards[card1])
// if card2 in cards:
//     card2 = int(cards[card2])
// if card3 in cards:
//     card3 = int(cards[card3])
if (card1 in cards) {
    card1 = cards[card1]
    
}
console.log(card1)
if (card2 in cards) {
    card2 = cards[card2]
    
}
console.log(card2)
if (card3 in cards) {
    card3 = cards[card3]
    
}
console.log(card3)


// total = int(card1) + int(card2) + int(card3)
let total = parseInt(card1) + parseInt(card2) + parseInt(card3)
console.log(total)

// if total < 17:
//     print(f'{total} - Hit')
// if total in range(17,21):
//     print(f'{total} - Stay')
// if total == 21:
//     print(f'{total} - Blackjack!')
// if total > 21:
//     print(f'{total} - Busted!')
if (total < 17) {
    alert(`${total} - Hit`)
}
if (total > 17 && total < 21) {
    alert(`${total} - Stay`)
}
if (total === 21) {
    alert(`${total} - Blackjack!!!`)
}
if (total > 21) {
    alert(`${total} - Busted!`)
}