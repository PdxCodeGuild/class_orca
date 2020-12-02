

function add(a, b) {
    return a + b;
}
console.log(add(5, 2));

// anonymous function
var add = function(a, b) {
    return a + b;
}; // this is a statement, and needs a semi-colon
console.log(add(5, 2));


let x = 10

function func() {
    x = 20 // ADD the 'let x = 20' will scope this var 'x' to this function
}
func()
// notice this will show x as 20 even though 
// thus you need to redefine variables in functions; it will change global variables othewise
console.log(x);

function getRandomInt(min, max) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min) + min); //The maximum is exclusive and the minimum is inclusive
  };

console.log(getRandomInt(1, 99));
