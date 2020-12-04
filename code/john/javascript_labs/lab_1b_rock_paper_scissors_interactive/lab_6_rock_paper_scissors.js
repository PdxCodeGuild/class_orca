// alert("hul111lo!");
// user_number1 = prompt("give me a number");  //this is like python's input('here')
// alert(`Your number is ${user_number1 * 10}`);

// alert(`Random number is ${random_number}`);
// I'm seeing ~18 digits commonly...

// var user_choice = prompt('Please type rock, paper, or scissors: ');
// let user_choice = 'rock';





    // PLAY() FUNCTION BEGIN
function play(user_choice) {
    console.log('play() function start')

    // let user_choice = button_paper.id
    
    computer_choice = '';
    var random_number = Math.random();
    if ( random_number  <= 0.3333333333333 ) {
        var computer_choice = 'rock' }
        else if ( random_number >= 0.33333333333333333333 && random_number <= 0.66666666666666666666 ) {
            var computer_choice = 'paper' }
        else if ( random_number >= 0.66666666666666666666 ) {
            var computer_choice = 'scissors' }
        else { var computer_choice = 'invalid!!' };
    console.log(`random_number: ${random_number}, computer_choice: ${computer_choice}, and user_choice: ${user_choice}.`);

    let p_text = document.createElement("p");
    if ( computer_choice === user_choice ) {
        p_text.innerText = `You cast ${user_choice}, and the computer chose ${computer_choice}. You tied! Statistically very likely and as boring as expected!`; }
        // console.log('You tied! Statistically very likely and as boring as expected!')
        
        else if ( user_choice === 'rock' && computer_choice === 'scissors') {
            p_text.innerText = `You cast ${user_choice}, and the computer chose ${computer_choice}. Your rock smashes feeble scissors and you win!`; }
            // console.log(`Your rock smashes feeble scissors and you win!`) 

        else if ( user_choice === 'rock' && computer_choice === 'paper') {
            p_text.innerText = `You cast ${user_choice}, and the computer chose ${computer_choice}. Nobody knows why paper wraps rock, but it does. You lose!`; }
            // console.log('Nobody knows why paper wraps rock, but it does. You lose!')
        
        else if ( user_choice === 'paper' && computer_choice === 'rock') { 
            p_text.innerText = `You cast ${user_choice}, and the computer chose ${computer_choice}. Nobody knows why paper wraps rock, but it does. You win!`; }
            // console.log('Nobody knows why paper wraps rock, but it does. You win!')

        else if (user_choice === 'paper' && computer_choice === 'scissors') { 
            p_text.innerText = `You cast ${user_choice}, and the computer chose ${computer_choice}. Computer cuts your paper. You lose!`; }
            // console.log('You lose!')

        else if (user_choice === 'scissors' && computer_choice === 'paper') {
        p_text.innerText = `You cast ${user_choice}, and the computer chose ${computer_choice}. You cut the paper and win!`; }
            // console.log('You cut the paper and win!')

        else if ( user_choice === 'scissors' && computer_choice === 'rock') {
        p_text.innerText = `You cast ${user_choice}, and the computer chose ${computer_choice}. Your scissors are broken to bits! You lose!`; }
            // console.log('Your scissors are broken to bits! You lose!')     

        else { 
            p_text.innerText = 'Invalid entry. Refresh page to try again!'};

    results.appendChild(p_text);
        // return something? ;
}
    // PLAY() FUNCTION FINISH ;



let button_rock = document.getElementById("rock");
let button_paper = document.getElementById("paper");
let button_scissors = document.getElementById("scissors");
// let button = document.getElementsByClassName("button_user_choice");
// console.log(`button: ${button} and button.id: ${button.id} and `); 

button_rock.addEventListener('click', function(e) {
    play("rock");
    // console.log(`user clicked: ${button.id} and computer_choice is ${computer_choice}`);
});

button_paper.addEventListener('click', function(e) {
    play("paper");
});

button_scissors.addEventListener('click', function(e) {
    play("scissors");
});