// alert("hul111lo!");
// user_number1 = prompt("give me a number");  //this is like python's input('here')
// alert(`Your number is ${user_number1 * 10}`);

var random_number = Math.random();
// alert(`Random number is ${random_number}`);
// I'm seeing ~18 digits commonly...

var user_choice = prompt('Please type rock, paper, or scissors: ');
// let user_choice = 'rock';

computer_choice = '';
if ( random_number  <= 0.3333333333333 ) {
    var computer_choice = 'rock' }
    else if ( random_number >= 0.33333333333333333333 && random_number <= 0.66666666666666666666 ) {
        var computer_choice = 'paper' }
    else if ( random_number >= 0.66666666666666666666 ) {
        var computer_choice = 'scissors' }
    else { var computer_choice = 'invalid!!' };
console.log(`The random number is ${random_number} and computer's choice is ${computer_choice}`);


// WORKING
if ( computer_choice === user_choice ) {
    alert('You tied! Statistically very likely and as boring as expected!') }
    
    else if ( user_choice === 'rock' && computer_choice === 'scissors') {
        alert(`Your rock smashes feeble scissors and you win!`) }
    else if ( user_choice === 'rock' && computer_choice === 'paper') {
        alert('Nobody knows why paper wraps rock, but it does. You lose!') }
    
    else if ( user_choice === 'paper' && computer_choice === 'rock') { 
        alert('Nobody knows why paper wraps rock, but it does. You win!') }
    else if (user_choice === 'paper' && computer_choice === 'scissors') { 
        alert('You lose!') }

    else if (user_choice === 'scissors' && computer_choice === 'paper') {
        alert('You cut and win!') }
    else if ( user_choice === 'scissors' && computer_choice === 'rock') { 
        alert('Your scissors are broken to bits! You lose!') }        

    else { alert('Invalid entry. Refresh page to try again!')};


// EXAMPLE:



// # https://github.com/PdxCodeGuild/Programming101/blob/master/labs/rps.md

// import random

// print('Welcome to rock, paper, scissors v1.57386.52.20200903!')
// user_choice = input('Please select your choice of rock, paper, or scissors: ')

// options = ['rock', 'paper', 'scissors']

// computer_choice = random.choice(options)
// print(f'The computer cast. . .: {computer_choice}') # firure out how to wait the text...

// if user_choice == 'rock' and computer_choice == 'scissors':
//     print('Your rock smashes feeble scissors and you win!')
// elif user_choice == 'rock' and computer_choice == 'paper':
//     print('Nobody knows why paper wraps rock, but it does. You lose!')
// elif user_choice == 'paper' and computer_choice == 'rock':
//     print('Nobody knows why paper wraps rock, but it does. You win!')
// elif user_choice == 'paper' and computer_choice == 'scissors':
//     print('You lose!')
// elif user_choice == 'scissors' and computer_choice == 'paper':
//     print('You rock and win!')
// elif user_choice == 'scissors' and computer_choice == 'rock':
//     print('Your scissors are broken to bits! You lose!')
// elif user_choice == computer_choice:
//     print('You tied! Statistically very likely but no less boring!')
// else:
//     print('Invalid entry!')
