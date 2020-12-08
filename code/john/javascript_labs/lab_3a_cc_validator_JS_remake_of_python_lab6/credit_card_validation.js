// REMEMBER TO ALWAYS END LINES WITH ; SEMICOLONS;
// REMEMBER TO ALWAYS END LINES WITH ; SEMICOLONS;

var valid_card_1 = '4077247134350245'; //# PASSED!
var valid_card_2 = '4281471859733607'; //# FAILED...
var valid_card_3 = '4318214376804015'; //# PASSED!
var valid_card_4 = '4527696733892419'; //# FAILED...
var invalid_card = '0102030405060708';

var easy_test_card = '0102030405060708';
var input_card_number = valid_card_3;
console.log(`Testing card #: ${input_card_number}`);

// #     STEP 1 Convert the input string into a list of ints
var test_card_array = input_card_number.split('');
console.log(`test_card_array: ${test_card_array}`);

// #     STEP 2 Slice off the last digit. That is the check digit
var check_digit = test_card_array.pop();
check_digit = parseInt(check_digit) // convert back
console.log(`check_digit is ${check_digit}, removed:`);
console.log(`test_card_array: ${test_card_array}`);

// #     STEP 3 Reverse the digits.
let test_card_array_reversed = JSON.parse(JSON.stringify(test_card_array)); //had to look this up!!
test_card_array_reversed.reverse();
console.log(`test_card_array_reversed is ${test_card_array_reversed}`);

// #     STEP 4 Double every other element in the reversed list.
// STEP 4A MAKE A NEW LIST
let temp_array_for_doubled_numbers = []
for ( let i=0; i<test_card_array_reversed.length; i++ ) { // part 1/3 initialization // part 2/3 condition // part 3/3 increment
    // console.log(`test_card_array_reversed[${i}] is ${test_card_array_reversed[i]}`)
    if ((i+1) % 2) { // every other
        console.log(`double this number: test_card_array_reversed[${i}] is ${test_card_array_reversed[i]}`);
        test_card_array_reversed[i] = test_card_array_reversed[i] * 2;
        // let temp_number = test_card_array_reversed[i] * 2 // make a temp number
        // console.log(`temp_number is ${temp_number}`);
        // temp_array_for_doubled_numbers.push(temp_number) // add that number to our temp array

        console.log(`test_card_array_reversed is NOW, CHANGED ${test_card_array_reversed}`);
    };
};
// STEP 4B POP ALL THE EITHER OR OUT
console.log(`test_card_array_reversed is NOW, CHANGED ${test_card_array_reversed}`);
// test_card_array_reversed.splice(13, 1); // remove this number
// test_card_array_reversed.splice(11, 1); // remove this number
// test_card_array_reversed.splice(09, 1); // remove this number
// test_card_array_reversed.splice(07, 1); // remove this number
// test_card_array_reversed.splice(05, 1); // remove this number
// test_card_array_reversed.splice(03, 1); // remove this number
// test_card_array_reversed.splice(01, 1); // remove this number
// console.log(`temp_array_for_doubled_numbers is ${temp_array_for_doubled_numbers}`);
console.log(`test_card_array_reversed is NOW, CHANGED ${test_card_array_reversed}`);
// STEP 4C (ONE LINE) COMBINE THE LISTS    
var array_step_5 = JSON.parse(JSON.stringify(test_card_array_reversed));
array_step_5 = array_step_5.concat(temp_array_for_doubled_numbers);
console.log(`array_step_5 is ${array_step_5} NOTE THAT THIS IS NOT IN ORDER!!!`); // NOTE THAT THIS IS NOT IN ORDER!!!


// #     STEP 5 Subtract nine from numbers over nine.
for ( let i=0; i<array_step_5.length; i++ ) {
    if (array_step_5[i] > 9) { 
        // console.log(`double this number: test_card_array_reversed[${i}] is ${test_card_array_reversed[i]}`);
        // let temp_number = array_step_5[i] * 2 // make a temp number
        // console.log(`temp_number is ${temp_number}`);
        array_step_5[i] = array_step_5[i] - 9
    };
};
console.log(`array_step_5 after numbers >9 -9 is ${array_step_5} NOTE THAT THIS IS NOT IN ORDER!!!`);


// #     STEP 6 Sum all values.
var sum_total = 0
var numbers_array = JSON.parse(JSON.stringify(array_step_5));
numbers_array.forEach(function(number) { // VERY VERY WIERD () {} SYNTAX!!! // used help in "ForEach" section at https://github.com/PdxCodeGuild/class_orca/blob/main/4%20JavaScript/docs/01f%20-%20Loops.md
    var number = parseInt(number); //convert string to integer... WHY it's a string in an array i dunno...never converted to integers?
    sum_total += number;
});
console.log(`sum_total is ${sum_total}`);

// #     STEP 7 Take the second digit of that sum.ta
let sum_as_string = sum_total.toString();
// console.log(`sum_as_string is ${sum_as_string}`);
let digit_2 = sum_as_string[1]
digit_2 = parseInt(digit_2) // convert back
console.log(`/////////////////////////////////////`);
console.log(`digit_2 is ${digit_2}`);
console.log(`typeof(check_digit) is ${typeof(check_digit)}`);
console.log(`typeof(digit_2) is ${typeof(digit_2)}`);



// / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 
// / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / / 


// #     STEP 8 If that matches the check digit, the whole card number is valid.
if ( digit_2 === check_digit ) {
    // alert('**********PASSED VALIDATION!**********')
    console.log('*PASSED VALIDATION!**');  }
    else {
        // alert('**********FAILED VALIDATION!**********');
        console.log('**********FAILED VALIDATION!**********');    };




// ///////////////////////////////////////////////////////
// EXAMPLE:
// EXAMPLE:
// EXAMPLE: