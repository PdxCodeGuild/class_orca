// This is part 2 of js lab 2. I used python lab 15 as the base. 
// Right now the entire program is converted into a function except for the
// the number to be entered. Which right now is in a do while loop.

function number_to_word (y) {
    let x = parseInt(y)
 
    let teens = {10:"ten",
     11:"eleven",
     12:"twelve", 
     13:"thirteen",
     14:"fourteen",
     15:"fifteen",
     16:"sixteen",
     17:"seventeen",
     18:"eightteen",
     19:"nineteen"}
 let first_digit = {1:"ten",
     2:"twenty",
     3:"thirty",
     4:"forty",
     5:"fifty",
     6:"sixty",
     7:"seventy",
     8:"eighty",
     9:"ninety"}
 let second_digit = {0:"zero",
     1:"one",
     2:"two",
     3:"three",
     4:"four",
     5:"five",
     6:"six",
     7:"seven",
     8:"eight",
     9:"nine",
     10:"ten"}
 
 if (100 <= x && x <= 999){
     if (1 <= (Math.floor(x / 100)) <= 9 && x % 100 === 0){
            console.log("wtf over 0?")
             return `${second_digit[(Math.floor(x / 100))]}-hundred`
     }else if ((x % 100) % 10 === 0){
            console.log("wtf over 1?")
             return `${second_digit[(Math.floor(x / 100))]}-hundred and ${first_digit[Math.floor((x % 100) / 10)]}`
     }else if (1<=(x % 100) && (x % 100)<= 9){
             console.log("wtf over 2?")
             return `${second_digit[(Math.floor(x / 100))]}-hundred and ${second_digit[(x % 100)]}`
     }else if (11<= (x % 100) && (x % 100) <= 19){
            console.log("wtf over 3?")
             return `${second_digit[(Math.floor(x / 100))]}-hundred and ${teens[(x % 100)]}`
     } else{
             return `${second_digit[(Math.floor(x / 100))]}-hundred ${first_digit[Math.floor((x % 100) / 10)]}-${second_digit[((x % 100) % 10)]}`
     }
 };

 if (x === 0){
     return second_digit[0]
 };
 if (Math.floor(x / 10) === 0){
     return second_digit[x]
 };
 if (x === 10){
     return teens[10]
 };
 if (11<= x && x <= 19){
    return teens[x]
 };
 if (20 <= x && x <= 99){
    return `${first_digit[(Math.floor(x / 10))]}-${second_digit[(x % 10)]}`
 };
 
}

// function is called number_to_word
let number = document.getElementById("thenumber");
let convert = document.getElementById("convert");
let results = document.getElementById("results");

convert.addEventListener("click", function(){
    // console.log(parseInt(number.value))
    if (parseInt(number.value)>= 0 && parseInt(number.value)<= 999){
        let message = number_to_word (parseInt(number.value))
        results.innerText = message
        number.value = ''
    }
    else if (parseInt(number.value) < 0 || parseInt(number.value) > 999) {
        // console.log('this is the else statement')
        let message = 'You must enter a number between 0-999'
        results.innerText = message
        number.value = ''
    }
})

number.addEventListener("keypress", function(event){
    // console.log(parseInt(number.value))
    if (event.key === 'Enter'){
        if (parseInt(number.value)>= 0 && parseInt(number.value)<= 999){
            let message = `${parseInt(number.value)} is ${number_to_word(parseInt(number.value))}!`
            results.innerText = message
            number.value = ''
        }
        else if (parseInt(number.value) < 0 || parseInt(number.value) > 999) {
            // console.log('this is the else statement')
            let message = 'You must enter a number between 0-999'
            results.innerText = message
            number.value = ''
        }
    }
})

//  input.addEventListener('keypress', function(event) {
    // if (event.key === 'Enter') {

    //     input.value = ''
// do {
// var y = prompt ("enter a number between 0 and 999:\n")
// }
// while (0 > parseInt(y) || parseInt(y) > 1000);
     
// alert(`${y} is ${number_to_word(y)}!`)