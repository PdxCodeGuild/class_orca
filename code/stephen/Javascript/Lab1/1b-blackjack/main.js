deck = {
    'A': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 10,
    'Q': 10,
    'K': 10,

};

let title =document.getElementById('title');
let topDiv = document.getElementById('topDiv');
let inputs = document.getElementById('inputs');
let btnsDiv = document.getElementById('btnsDiv');
let btn = document.getElementById('btn');
let adviceDiv = document.getElementById('adviceDiv');
let adviceP = document.getElementById('adviceP');
let hitDiv = document.getElementById('hitDiv');
let hitP = document.getElementById('hitP');
let hitP2 = document.getElementById('hitP2');
let hitAdvice = document.getElementById('hitAdvice');
let headpic = document.getElementById('headpic');
let cardInput = document.getElementsByClassName('cardInput');

document.body.style.backgroundColor = "#35654d";
document.body.style.display = "flex";
document.body.style.flexDirection = "column";
document.body.style.alignItems = "center";
document.body.style.textAlign = "center";
document.body.style.color = "whitesmoke";
title.style.fontSize = "44px";
document.body.style.fontSize = "24px";
headpic.style.width = "100%";


function pickRandomCard(obj) {
    var result;
    var count = 0;
    for (var x in obj)
        if (Math.random() < 1/++count)
           result = x;
    return result;
}

btn.addEventListener('click', function() {
    var x = document.getElementsByClassName('cardInput');
    var card1 = cardInput[0].value;
    var card2 = cardInput[1].value;
    var card3 = cardInput[2].value;

    if (card1 in deck) {
        card1 = deck[card1];
        console.log(card1)
    }
    
    if (card2 in deck) {
        card2 = deck[card2];
        console.log(card2)
    }

    if (card3 in deck) {
        card3 = deck[card3];
        console.log(card3)
    }

    let total = card1 + card2 + card3;
    console.log(total)

    if (total < 17) {
        adviceP.innerText = `You have ${total}!  My advice is to hit!`
        var hitBtn = document.createElement("BUTTON");
        var t = document.createTextNode("Hit!");
        hitBtn.appendChild(t);
        document.body.appendChild(hitBtn);
        
    }
    if (total >= 17 && total < 21) {
        adviceP.innerText = `You have ${total}!  My advice is to stay!`
    }
    if (total === 21) {
        adviceP.innerText = `${total}!  Blackjack!`
    }
    if (total > 21) {
        adviceP.innerText = `You have ${total}!  You busted!`
    }

    hitBtn.addEventListener('click', function() {
        hitBtn.style.display = 'none';
        rando = pickRandomCard(deck);
        hitP.innerText = `You drew a ${rando}`
        // console.log(rando)
        if (rando in deck) {
            rando = deck[rando]
            console.log(rando)
        }
        var newTotal = total + rando
        console.log(newTotal)
        // hitP2.innerText = `Your new total is ${newTotal}` 
        if (newTotal < 17) {
            hitAdvice.innerText = `You have ${newTotal}!  My advice is to hit!`
            var hitBtn2 = document.createElement("BUTTON");
            var t = document.createTextNode("Hit!");
            hitBtn2.appendChild(t);
            document.body.appendChild(hitBtn2);
            
        }
        if (newTotal >= 17 && newTotal < 21) {
            hitAdvice.innerText = `You have ${newTotal}!  My advice is to stay!`
        }
        if (newTotal === 21) {
            adviceP.innerText = `${newTotal}!  Blackjack!`
        }
        if (newTotal > 21) {
            hitAdvice.innerText = `You have ${newTotal}!  You busted!`
        }
        hitBtn2.addEventListener('click', function() {
            hitBtn2.style.display = 'none';
            rando2 = pickRandomCard(deck);
            hitP.innerText = `You drew a ${rando2}`
            // console.log(rando)
            if (rando2 in deck) {
                rando2 = deck[rando2]
                // console.log(rando)
            }
            var newTotal2 = newTotal + rando2
            // console.log(newTotal)
            hitP2.innerText = `Your new total is ${newTotal2}`
            if (newTotal2 < 17) {
                hitAdvice.innerText = `You have ${newTotal2}!  My advice is to hit!`
                var hitBtn3 = document.createElement("BUTTON");
                var t = document.createTextNode("Hit!");
                hitBtn3.appendChild(t);
                document.body.appendChild(hitBtn3);
                
            }
            if (newTotal2 >= 17 && newTotal2 < 21) {
                hitAdvice.innerText = `You have ${newTotal2}!  My advice is to stay!`
            }
            if (newTotal2 === 21) {
                adviceP.innerText = `${newTotal2}!  Blackjack!`
            }
            if (newTotal2 > 21) {
                hitAdvice.innerText = `You have ${newTotal2}!  You busted!`
            }
            hitBtn3.addEventListener('click', function() {
                hitBtn3.style.display = 'none';
                rando3 = pickRandomCard(deck);
                hitP.innerText = `You drew a ${rando3}`
                // console.log(rando)
                if (rando3 in deck) {
                    rando3 = deck[rando3]
                    // console.log(rando)
                }
                var newTotal3 = newTotal2 + rando3
                // console.log(newTotal)
                hitP2.innerText = `Your new total is ${newTotal3}`
                if (newTotal3 < 17) {
                    hitAdvice.innerText = `You have ${newTotal3}!  We're done!`
                    
                    
                }
                if (newTotal3 >= 17 && newTotal3 < 21) {
                    hitAdvice.innerText = `You have ${newTotal3}!  My advice is to stay!`
                }
                if (newTotal3 === 21) {
                    adviceP.innerText = `${newTotal3}!  Blackjack!`
                }
                if (newTotal3 > 21) {
                    hitAdvice.innerText = `You have ${newTotal3}!  You busted!`
                }
            })
        })
    })
})
