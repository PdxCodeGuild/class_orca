
//  *'-.-'*'-.-'*'-.-'*-.-'*-.-'*-.-'*-.-'*'-.-'*'-.-'*'-.-'*
//         Project: Javascript
//  Assignment/Ver: Lab 1b
//          Author: Ron Mansolilli, ron.mansolilli@gmail.com
//            Date: 12-1-2020
//  *'-.-'*'-.-'*'-.-'*-.-'*-.-'*-.-'*-.-'*'-.-'*'-.-'*'-.-'*

// ----Instructions and notes--------------------------------

/* Pick 6 (from Python Lab 14) */

// ----Global variables, lists, dictionaries------------------

let nums = [5, 0, 8, 3, 4, 1, 6];   // Data for version 1
let x = 0;                          // Loop iteration 
let num_list = [];                  // Data holder version 2
let i = true;                       // While loop condition

// ----Functions----------------------------------------------

/* None */

// ----Main Code---------------------------------------------

/* Version 1 */

    nums.forEach(function(nums) {
        x += nums; 
    });
    let y = x / (nums.length);

/* Version 2 */
    x = 0;
    let z = 0;

    while (i) {
        user_input = prompt('Enter a number, or done: ');
        if (user_input === 'done') {
            num_list.forEach(function(num_list) {
                x += num_list; 
            });
            z = x / (num_list.length);
            i = false;
        } else {
            let b = parseInt(user_input);
            num_list.push(b);
            console.log(num_list);
        }
    }

/* Output */

alert(`Lab 10 \n\n Version 1 \n ----------\n Average of (${nums}): ${y = y.toFixed(2)} 
     \nVersion 2 \n ----------\n Average of (${num_list}): ${z = z.toFixed(2)} `);







