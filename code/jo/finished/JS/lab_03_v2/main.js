let c1 = document.getElementById('c1')
let c2 = document.getElementById('c2')
let c3 = document.getElementById('c3')
let btn = document.getElementById('btn')
let advice = document.getElementById('advice')

btn.addEventListener('click', function(){
    let values = {"A": 1,"2": 2,"3": 3,"4": 4,"5": 5,"6": 6,"7": 7,"8": 8,"9": 9,"J": 10,"Q": 10,"K": 10,
    };
    let total_value = values[c1.value] + values[c2.value] + values[c3.value]
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
    alert(`Your total value is ${total_value}. ${action}`)
})
