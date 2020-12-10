alert('Lets play Rock, Paper, Scissors!')

let choices = ['rock', 'paper', 'scissors']

function choose(choices) {
    let index = Math.floor(Math.random() * choices.length);
    choice = choices[index]
    return choice;
}

let computer = choose(choices)

let your_choice = prompt('Rock, Paper or Scissors?')
your_choice = your_choice.toLowerCase()

if (your_choice == computer) {
    alert(`I chose ${computer}. You chose ${your_choice}. It's a tie!`)
} else if (your_choice == 'rock' && computer == 'scissors' || your_choice == 'paper' && computer == 'rock' || 
            your_choice == 'scissors' && computer == 'paper') {
    alert(`I chose ${computer}. You chose ${your_choice}. You win!`)
} else {
    alert(`I chose ${computer}. You chose ${your_choice}. I win!`)
}
