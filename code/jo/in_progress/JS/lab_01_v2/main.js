// number averager

let add_btn = document.getElementById("add_btn");
let avg_btn = document.getElementById("avg_btn");
let num = document.getElementsByClassName("num");
let average = document.getElementById("average");
let numbers = [];
let avg = 0;
let sum = 0;

// inputs from num are objects not ints.
function doAverage(e) {
    console.log(num)
    let li = document.createElement('li');
    numbers.push(num)
    for (let i=0; i<nu)
    // if (Number.isInteger(+num)) {
    //     numbers.push(num);
    // };
    // numbers.forEach(function(i) { 
    //     sum += (+i);
    });

    avg += ((+sum) / (+numbers.length));

    li.innerText = (`The average of ${numbers} is ${avg}`);
    average.appendChild(li);
    console.log(sum);
    console.log(numbers);
    console.log(avg);
};

add_btn.addEventListener('click', doAverage);




// if (Number.isInteger(+add_num)) {
//     num.push(add_num);

// num.forEach(function(i) {
//     total += (+i);

// function doAverage(e) {
//     let li = document.createElement('li');
//     let sum = 0;
//     let avg = 0;
//     let num = document.getElementById('num');
//     for (let i=0; i<num.length; i++) {
//         if (num[i].value) {
//             sum += parseFloat(nums[i].value);
//             avg += sum / num.length;
//         }
//     }
//     li.innerText = (`The average is ${sum}`);
//     average.appendChild(li);
// }

// let add = document.getElementById("add");
// let average = document.getElementById("average");
// let numbers = document.getElementsByClassName("numbers");
// let num = document.getElementById("num");

// function doAverage(e) {
//     let li = document.createElement('li');
//     let numbers = document.getElementsByClassName('numbers');
//     let sum = 0;
    
//     for (let i=0; i<numbers.length; i++) {
//         if (numbers[i].value) {
//             sum += parseFloat(numbers[i].value)
//         }; 
//     };
//     let average = 0;
//     average += sum / numbers.length;
//     li.innerText = (`The average of ${numbers} is ${average}.`);
//     numbers.appendChild(li);
// };

// average.addEventListener('click', doAverage);

// add.addEventListener('click', function(e) {

// })





// // # an empty list to add to
// let num = [];

// // # loop to keep asking for input until entering done
// let input = true;
// while (input) {
//     let add_num = prompt('Enter a number to add it to the list and type "done" when finished ');
//     if (Number.isInteger(+add_num)) {
//         num.push(add_num);
//     } else if (add_num === 'done') {
//         input = false;
//     }
// }

// // # establishes a variable of zero to add values of list to
// let total = 0

// //  # for each item in list, will continue to add them to each other to get a total
// num.forEach(function(i) {
//     total += (+i);
// });
// console.log(total);

// // # divide the sum of all numbers by the number if items in the list to get the avearage
// let average = total / num.length;

// // # print it out
// alert(`Your list of ${num} had a total of ${total} for an average of ${average}`);