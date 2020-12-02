
// randomizer (but not including 1)
console.log(Math.floor(Math.random()*10))

let name = 'Juice';
console.log(`Hello! My name is ${name}!`)

let temp = 49

if (temp > 32) { // example of if statement and difference with python i.e. if temp > 32;
    console.log("It is above freezing") // <tab> print("...")
}

let comfort = temp > 65 ? true : false // same type of conditional expression in python, but more terse
console.log(comfort)

let fruits = ['apple', 'bananana', 'pear'];
fruits.push('cherry');

// Notice the 3 parts; 1) declare 2) set conditional 3) iteration.  Then the other actions occur.  
for (let i=0; i<fruits.length; i++) {
    console.log(fruits[i]);
}
console.log(fruits.indexOf('apple')); // should print 0

let fruits1 = ['guava', 'grape', 'lemon'];

fruits1.forEach(function(fruits1) {
    console.log(fruits1); 
});

// array1.forEach(element => console.log(element));
