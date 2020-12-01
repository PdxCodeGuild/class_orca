

// # an empty list to add to
// num = []
let num = [];

// # adds user input to the list
// add_num = input('Enter a number to add it to the list and type "done" when finished ')

// # loop to keep asking for input until entering done
// while add_num != 'done':
//     num.append(add_num)
//     add_num = input('Enter a number to add it to the list and type "done" when finished ')

let input = true;
while (input) {
    let add_num = prompt('Enter a number to add it to the list and type "done" when finished ');
    if (Number.isInteger(+add_num)) {
        num.push(add_num);
    } else if (add_num === 'done') {
        input = false;
    }
}

// # establishes a variable of zero to add values of list to
// total = 0
let total = 0

//  # for each item in list, will continue to add them to each other to get a total
// for i in range(len(num)):
//     total += int(num[i])
num.forEach(function(i) {
    total += (+i);
});
console.log(total);
// # divide the sum of all numbers by the number if items in the list to get the avearage
// average = total / len(num)
let average = total / num.length;

// # print it out
// print(f'The average of the list is {average}')
alert(`Your list of ${num} had a total of ${total} for an average of ${average}`);