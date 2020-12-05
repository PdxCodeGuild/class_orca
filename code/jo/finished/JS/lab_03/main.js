
// # dictionary assigning values to cards
// values = {
//     "A": 1,
//     "2": 2,
//     "3": 3,
//     "4": 4,
//     "5": 5,
//     "6": 6,
//     "7": 7,
//     "8": 8,
//     "9": 9,
//     "J": 10,
//     "Q": 10,
//     "K": 10
// }
let values = {
    "A": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "J": 10,
    "Q": 10,
    "K": 10,
};

// # input asks for cards user has
// card_1 = input("What is your first card? ")
// card_2 = input("What is your second card? ")
// card_3 = input("What is your third card? ")
let card_1 = prompt("What is your first card?");
let card_2 = prompt('What is your second card?');
let card_3 = prompt('What is your third card?');

// # gets values of inputs from dictionary and adds them together
// total_value = values[card_1] + values[card_2] + values[card_3]
let total_value = values[card_1] + values[card_2] + values[card_3];

// # checks the total value against some comparisons to determine best advice
// if total_value < 17:
//     action = 'You should hit.'
// elif 17 <= total_value <= 20:
//     action = 'You should stay.'
// elif total_value == 21:
//     action = 'You got Blackjack!'
// else:
//     action = 'You\'re already busted'
let action = ''
if (total_value < 17) {
    action += 'you should hit.';
} else if (17 <= total_value <= 20) {
    action += 'you should stay';
} else if (total_value === 21) {
    action += "you got blackjack!";
} else {
    action += "you're already busted";
};

// # prints out the total value and advice
// print (f"Your total value is {total_value}. {action}")
alert(`Your total value is ${total_value}. ${action}`)