//#This is part 2 of creating the javascript lab creating an actual web interface
// This is a java script version of the black jack lab, The python code is copied below
// This is Lab 19 Black Jack Advice Version 1
// def main():
//     def b_j_a(x):
//         if x < 17:
//             return "Hit!"
//         if 17 < x < 21:
//             return "Stay!"
//         if x == 21:
//             return "Blackjack! You lucky S.O.B."
//         if x > 21:
//             return "You busted! Time to find an ATM"
//     deck = {"J":10,
//     "Q":10,
//     "K":10,
//     "A":1,
//     "9":9,
//     "8":8,
//     "7":7,
//     "6":6,
//     "5":5,
//     "4":4,
//     "3":3,
//     "2":2}
//     card_1 = input("What is your first card: A, K, Q, J or 1 - 9?\n") 
    
//     if card_1 not in deck:
//         while card_1 not in deck:
//             print ("What kind of deck is this? Try Again.\n")
//             card_1 = input("What is your first card: A, K, Q, J or 1 - 9?\n")
//     if card_1 in deck:
//         card_1 = deck[card_1]
    
//     card_2 = input("What is your second card: A, K, Q, J or 1 - 9?\n") 
    
//     if card_2 not in deck:
//         while card_2 not in deck:
//             print ("What kind of deck is this? Try Again.\n")
//             card_2 = input("What is your second card: A, K, Q, J or 1 - 9?\n")
//     if card_2 in deck:
//         card_2 = deck[card_2]
    
//     card_3 = input("What is your third card: A, K, Q, J or 1 - 9?\n") 
    
//     if card_3 not in deck:
//         while card_3 not in deck:
//             print ("What kind of deck is this? Try Again.\n")
//             card_3 = input("What is your second card: A, K, Q, J or 1 - 9?\n")
//     if card_3 in deck:
//         card_3 = deck[card_3]
//     x = (card_1 + card_2 + card_3)
//     print(b_j_a(x))

// main()

// def b_j_a(x):
//         if x < 17:
//             return "Hit!"
//         if 17 < x < 21:
//             return "Stay!"
//         if x == 21:
//             return "Blackjack! You lucky S.O.B."
//         if x > 21:
//             return "You busted! Time to find an ATM"

function hit_or_stay(x) {
    if (x < 17 ) {
        return (`You have ${x}, Hit!`)
    } else if (17 < x < 21){
        return(`You have ${x}, Stay!`) 
    } else if (x===21){
        return(`You have ${x}, Blackjack! You lucky S.O.B.!`)
    } else if (x > 21){
        return(`You have ${x}, You busted!`)
    }
}

let deck = {
    "J":10,
    "Q":10,
    "K":10,
    "A":1,
    "9":9,
    "8":8,
    "7":7,
    "6":6,
    "5":5,
    "4":4,
    "3":3,
    "2":2}

    //     card_1 = input("What is your first card: A, K, Q, J or 1 - 9?\n") 
// let btn = document.getElementById("btn");
let more = document.getElementById("more");
let cards = document.getElementsByClassName("card");
let check = document.getElementById("Check my cards");
let inputs = document.getElementById("inputs");
let card = document.getElementById("dropdown");
let results = document.getElementById("results");
let card_1_select = document.getElementById("cardname1");
let card_2_select = document.getElementById("cardname2");

// let x = card_1 + card_2

check.addEventListener("click", function(){
    let x = deck[card_1_select.value] + deck[card_2_select.value]
    let message = hit_or_stay(x); 
    results.innerText = message

    // console.log(x);
    console.log(card_1_select.value);
    console.log(card_2_select.value);
})


//     console.log(e)
// })
// results.addEventListener('click', function(e){
//     console.log(card.value)
//     console.log(e)
// })

// let card_1 = prompt ("What is your first card: A, K, Q, J or 1 - 9?\n"); 
// let card_1a = deck[card_1];
// let card_2 = prompt ("What is your second card: A, K, Q, J or 1 - 9?\n");
// let card_2a = deck[card_2];
// let card_3 = prompt ("What is your third card: A, K, Q, J or 1 - 9?\n");
// let card_3a= deck[card_3]; 

// let x = (card_1a + card_2a + card_3a)

// hit_or_stay(x)

// if (card_1 in deck){
// console.log(deck[card_1])
// }
// if card_1 not in deck:
//         while card_1 not in deck:
//             print ("What kind of deck is this? Try Again.\n")
//             card_1 = input("What is your first card: A, K, Q, J or 1 - 9?\n")
//     if card_1 in deck:
//         card_1 = deck[card_1]


// From Marc Lowe to Everyone:  04:34 PM
// I just had a quick question about JavaScript and objects.
// From Austen Cote to Me:  (Privately) 04:59 PM
// const thing1 = '7'
// const thing2 = 'A'
// // the above sets the unchangable var of card1 and card2

// const stuff = { A: 1, 7: 7, 9: 9 }
// // this represents the card object where the key is user_input val int representation

// const things = [parseInt(thing1), thing2]
// // this is the arr of the int values of the user input 
// let count = 0
// // this is the inital count 

// for (let i = 0; i <= things.length - 1; i++) {
//   // initalizing i to value of 0
//   // while i is less than or equal to the length of things -1 
//   // then add 1 to i
//   console.log(stuff[things[i]])
//   count += stuff[things[i]]
//   // stuff is the object[things is the arr [i is the current val]]
// }
// console.log(count, 'the count is')
