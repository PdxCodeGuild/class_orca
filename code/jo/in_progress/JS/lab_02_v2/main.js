// # gets cc# from input
// cc_num = input("What is your credit card number? ")
let cc_num = prompt('What is your credit card number? 4556737586899855');

// # turns number into a list, converts to int, saves last number, removes last number, and reverses it all
// cc_num = list(cc_num)
// cc_num = [int(num) for num in cc_num]
// check_num = cc_num.pop()
// cc_num.reverse()

let cc_split = cc_num.split("");
let cc_int = [];
cc_split.forEach(function(i) {
    cc_int.push(+i);
});
let check_num = cc_int[15];
cc_int.pop();
cc_int.reverse();

// # doubles every other number
// # for i,num in enumerate(cc_num):
// #     if i % 2 == 0:
// #        cc_num[i] *= 2
// cc_num = [num *2 if i % 2 == 0 else num for i,num in enumerate(cc_num)]
for (let i=0; i<cc_int.length; i++) {
    if (i % 2 === 0) {
        cc_int[i] *=2;
    }
}

console.log(cc_int);

// # subtracts 9 from any numbers over 9
// cc_num = [i - 9 if i >9 else i for i in cc_num]
for (let i=0; i<cc_int.length; i++) {
    if (cc_int[i] > 9) {
        cc_int[i] = cc_int[i] - 9;
    }
}

console.log(cc_int);

// # adds all numbers in list together to get a number to compare to the check number
// comp_num = sum(cc_num)
let comp_num = 0;
cc_int.forEach(function(i) {
    comp_num += (+i);
});

console.log(comp_num);

// # isolates the second digit and compares it to check number and prints valid or not
// if comp_num % 10 == check_num:
//     print("Valid!")
// else:
//     print("Not Valid.")
if (comp_num % 10 === check_num) {
    alert("Valid!");
}
else {
    alert('Not valid!')
}


