const container = document.getElementById('container')
const matchForm = document.getElementById('matchForm')

//Display info in DOM
let btn = document.getElementById("btn");
btn.addEventListener('click', function() {
    pick_6();
    const yourTicket = document.getElementById('yourTicket')
    yourTicket.innerText = `Your ticket is: ${ticket}`
    getLotto();
    const lottoNums = document.getElementById('winners')
    lottoNums.innerText = `The winning numbers are: ${winning_numbers}`  
    calcMatch(ticket, winning_numbers);
    const matches = document.getElementById('matches');
    matches.innerText = `You have: ${count} matches`  
});

//Display winnings info
let whatif = document.getElementById("whatif");
whatif.addEventListener('click', function() {
    calcWinnings();
    const showWinnings = document.getElementById('show-winnings')
    showWinnings.innerText = `You lost $${earnings}`
    const showROI = document.getElementById('roi')
    showROI.innerText = `Your roi was: ${roi}%`
    showWinnings.style.color = "lime";
    showROI.style.color = "lime";
});


//Generate lotto numbers 
function getRandomInt(min, max) {
    return Math.floor(Math.random() * (max - min) + min);
}

function getLotto() {
    let lotto_1 = getRandomInt(1, 100);
    let lotto_2 = getRandomInt(1, 100);
    let lotto_3 = getRandomInt(1, 100);
    let lotto_4 = getRandomInt(1, 100);
    let lotto_5 = getRandomInt(1, 100);
    let lotto_6 = getRandomInt(1, 100);
    
    let winning_numbers = [lotto_1, lotto_2, lotto_3, lotto_4, lotto_5, lotto_6]

    return winning_numbers
};
winning_numbers = getLotto()
console.log(winning_numbers);

let score = [];
let count = 0;
let choice_1 = 0;
let choice_2 = 0;
let choice_3 = 0;
let choice_4 = 0;
let choice_5 = 0;
let choice_6 = 0;
ticket = []

// Generate lotto ticket
function pick_6() {
    let choice_1 = getRandomInt(1, 100);
    let choice_2 = getRandomInt(1, 100);
    let choice_3 = getRandomInt(1, 100);
    let choice_4 = getRandomInt(1, 100);
    let choice_5 = getRandomInt(1, 100);
    let choice_6 = getRandomInt(1, 100);

    let ticket = [choice_1, choice_2, choice_3, choice_4, choice_5, choice_6]

    return ticket
};

ticket = pick_6()

console.log(ticket);

// Calculate matching numbers
function calcMatch(ticket, winning_numbers){
    let score = [];
    let count = 0;

    for (let i =0; i < ticket.length; i++) {
        if (ticket[i] == winning_numbers[i]) {
            score.push(ticket[i])
            count++
        }
    }
    return count
};

count = calcMatch(ticket, winning_numbers)
// console.log(count)

// Calculate winnings
let balance = 0;
let balance_debit = 0;
let new_balance = 0;
let total_count = 0;
let loop_count = 0;
let instance_total = 0;
let earnings = 0;
let roi = 0;

function calcWinnings() {
    for (let i = 0; i < 10000; i++) {
        loop_count += 1  
        winning_numbers = getLotto() 
        ticket = pick_6() 
        count = calcMatch(ticket, winning_numbers)
        total_count += instance_total

        if (count == 1) {
            new_balance += 4
        };
        
        if (count == 2) {
            new_balance += 7
        };
        
        if (count == 3) {
            new_balance += 100
        };
        
        if (count == 4) {
            new_balance += 50000
        };

        if (count == 5) {
            new_balance += 100000
        };
        
        if (count == 6) {
            new_balance += 25000000
        };
    
        balance_debit -= 2
    }
    earnings = (balance_debit + new_balance) * -1
    let roi = earnings / balance_debit

    console.log(earnings)
    return earnings

    // alert(`You earned: ${earnings} dollars after 10,000 tries`)
    // alert(`Your roi was: ${roi}%`)
    // return roi
};
