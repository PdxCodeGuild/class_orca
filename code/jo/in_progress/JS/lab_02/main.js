// # gets cc# from input
// cc_num = input("What is your credit card number? ")
let cc_num = prompt('What is your credit card number? 4556737586899855');

// # turns number into a list, converts to int, saves last number, removes last number, and reverses it all
// cc_num = list(cc_num)
// cc_num = [int(num) for num in cc_num]
// check_num = cc_num.pop()
// cc_num.reverse()

let cc_array = cc_num.split("");

console.log(cc_array);



// # doubles every other number
// # for i,num in enumerate(cc_num):
// #     if i % 2 == 0:
// #        cc_num[i] *= 2
// cc_num = [num *2 if i % 2 == 0 else num for i,num in enumerate(cc_num)]

// # subtracts 9 from any numbers over 9
// cc_num = [i - 9 if i >9 else i for i in cc_num]

// # adds all numbers in list together to get a number to compare to the check number
// comp_num = sum(cc_num)

// # isolates the second digit and compares it to check number and prints valid or not
// if comp_num % 10 == check_num:
//     print("Valid!")
// else:
//     print("Not Valid.")

