let card = [];
let hand = [];
let cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10',];
let faceCards = ['j', 'q', 'k']


let prom = document.getElementById("prom")
let input = document.getElementById("input")
let btn = document.getElementById("btn")
let output = document.getElementById("output")

let remove_btn = document.getElementById("remove_btn") 

let counter = 0
btn.addEventListener('click', function() {


    if (counter === 0){
        prom.innerText = "Please enter your Second Card"
        counter += 1
        // This line communicated to the HTML and says push or append it in
        card.push(input.value)
        console.log(card)

        valueOfHand(input.value)
    }
    else if (counter === 1){
        prom.innerText = "Please enter your Third Card"
        counter += 1
        // This line communicated to the HTML and says push or append it in
        card.push(input.value)
        console.log(card)

        valueOfHand(input.value)
    }
    else if (counter > 1){
        remove_btn.removeChild(btn)
        // This line communicated to the HTML and says push or append it in
        card.push(input.value)
        console.log(card)
        
        valueOfHand(input.value)
        addingHand()
        advisor()
    }
let displayText = document.createElement('p')
displayText.innerText = `You have a ${input.value}` 

// This is what it makes <p> text inside</p>
output.appendChild(displayText)
 

})

let valueOfHand = function (card) {
    console.log(typeof(card))
    if (faceCards.includes(card)){
        card = 10
        hand.push(card)
        // console.log(hand)
        }

    else if (cards.includes(card)){
        card = parseInt(card)
        hand.push(card)
    }

    else if (card === 'a'){
        card = 1
        hand.push(card)
        console.log(hand)
    }

    else{
        alert('enter valid card')
        alert("what is your first card ie. (a, 2, 3, 4, 5, 6, 7, 8, 9, 10, j, q, or k): ")
    }   
}


let addingHand = function() {
    let handSum = hand[0] + hand[1] + hand[3]
}

let advisor = function() {
    let total = 0
    for (let index = 0; index < hand.length; index++) {
        let card = hand[index]
        total += card
    }

    if (total < 17){
        let resultsText = document.createElement('p')
        resultsText.innerText = "Hit: The sum of your cards are less than 17" 
        adviceOutput.appendChild(resultsText)
    }

    else if (total >= 17 && total < 21){
        let resultsText = document.createElement('p')
        resultsText.innerText = "Stay: The sum of your cards are between 17 and 21" 
        adviceOutput.appendChild(resultsText)
    }

    else if (total == 21){
    let resultsText = document.createElement('p')
    resultsText.innerText = "Blackjack: The sum of your cards is 21"
    adviceOutput.appendChild(resultsText)
    }

    else if (total > 21){
        let resultsText = document.createElement('p')
        resultsText.innerText = "Busted: The sum of your cards is above 21"
        adviceOutput.appendChild(resultsText)
    }
}


