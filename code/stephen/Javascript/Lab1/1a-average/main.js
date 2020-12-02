let nums = [];

let done = false;

while (done == false) {
    let user_num = prompt('Enter in a number or type done to get your average of input numbers: ');
    if (user_num == 'done'){
        done = true;
    } else {
        user_num = parseInt(user_num);
        nums.push(user_num);
    }

}
console.log(nums)
let total = 0;

let sum = nums.reduce(function(a, b) {
    return a + b;
}, 0);
console.log(sum)
let len = nums.length;
let average = sum/len;
let avg = average.toFixed(2);
alert(`You input ${len} numbers totalling ${sum}!  The average is ${avg}!`)