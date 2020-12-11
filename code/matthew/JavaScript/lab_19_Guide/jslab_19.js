
var user_input = function() {
    var cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10',];
    var hand = []
    var faceCards = ['j', 'q', 'k']
    var count = 0
    let card = prompt("what is your first card, a, 2, 3, 4, 5, 6, 7, 8, 9, 10, j, q, or k ");
    
    if (faceCards.includes(card)){
        // alert("This worked")
        card = 10
        hand.push(card)
        }

    else if (cards.includes(card)){
        card = parseInt(card)
        hand.push(card)
    }

    else if (card === 'a'){
        card = 1
        hand.push(card)
    }

    else{
        alert('enter valid card')
        alert("what is your first card ie. (a, 2, 3, 4, 5, 6, 7, 8, 9, 10, j, q, or k): ")
    }

    alert(hand)


}

var count_card = function() {
    let total = 0
    for (let index = 0; index < hand.length; index++) {
        let card = hand[index]
        total += card
    }

    if (total < 17){
        alert("hit")
    }

    else if (total >= 17 && total < 21){
        alert("stay")
    }

    else if (total == 21){
        alert("blackjack!")      
    }

    else if (total > 21){
        alert("busted")
    }
}

let runFucntion = function() {
    while (count < 3) {
        count ++
        user_input();

        if (count == 3) {
            count_card();
        }
    }
}

let prom = document.getElementById("prom")
let input = document.getElementById("input")
let btn = document.getElementById("btn")
let output = document.getElementById("output")

let remove_btn = document.getElementById("remove_btn") 
let counter = 0

btn.addEventListener('click', function() {
    console.log(counter)

    if (counter === 0){
        prom.innerText = "Please enter your Second Card"
        counter += 1

    }
    else if (counter === 1){
        counter += 1
        prom.innerText = "Please enter your Third Card"
    }
    else if (counter > 1){
        remove_btn.removeChild(btn)
    }
    
let displayText = document.createElement('p')
displayText.innerText = `You have a ${input.value}` 
// This is what it makes <p> text inside</p>
output.appendChild(displayText) 
// This line communicated to the HTML and says push or append it in
})