let choices = ['rock', 'paper', 'scissors'];
let user_input = document.getElementById('user_input');
let play = document.getElementById('play');
let computer_choice = document.getElementById('computer_choice');

function choose(choices) {
    let index = Math.floor(Math.random() * choices.length);
    choice = choices[index]
    return choice;
};

let computer = choose(choices);

play.addEventListener('click', function() {
    if (user_input.value === computer) {
        computer_choice.innerText = `I choose ${computer}.\nIt's a tie!`
    } else if (user_input.value === 'rock' && computer === 'scissors' || user_input.value ===  'paper' && computer === 'rock' || 
                user_input.value === 'scissors' && computer === 'paper') {
        computer_choice.innerText = `I choose ${computer}.\nYou win!`
    } else {
        computer_choice.innerText = `I choose ${computer}.\nI win!`
}})

user_input.addEventListener('keydown', function(e) {
    if (e.key === "Enter") {
        if (user_input.value === computer) {
            computer_choice.innerText = `I choose ${computer}.\nIt's a tie!`
        } else if (user_input.value === 'rock' && computer === 'scissors' || user_input.value ===  'paper' && computer === 'rock' || 
                    user_input.value === 'scissors' && computer === 'paper') {
            computer_choice.innerText = `I choose ${computer}.\nYou win!`
        } else {
            computer_choice.innerText = `I choose ${computer}.\nI win!`
    }
    }
})