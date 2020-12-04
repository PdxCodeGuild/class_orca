
/*'-.-'*'-.-'*'-.-'*-.-'*-.-'*-.-'*-.-'*'-.-'*'-.-'*'-.-'*/
//         Project: Javascript
//  Assignment/Ver: Lab 2a
//          Author: Ron Mansolilli, ron.mansolilli@gmail.com
//            Date: 12-02-2020
/*'-.-'*'-.-'*'-.-'*-.-'*-.-'*-.-'*-.-'*'-.-'*'-.-'*'-.-'*/

/* ----Instructions and notes--------------------------------
 
    Unit Converter (from Python Lab 10) 
    ... utilize the input and button elements. 

*/
// ----Global variables, lists, dictionaries------------------

let nums = [5, 0, 8, 3, 4, 1, 6];   // Data for version 1

    // ** Also see declarations below **

/* ----Functions----------------------------------------------

    None - see below

*/
// ----Main Code---------------------------------------------

/* Version 1 *////////////////////////////////////////////////////

    //Declarations
    let bt1 = document.getElementById('bt1');
    let results1 = document.getElementById('results1');
    let list1 = document.getElementById('list1')
    let x = 0;

    //Code
    nums.forEach(function(nums) {
        x += nums; 
    });
    let y = x / (nums.length);
    console.log(y)

    //Formatting and Events
    list1.innerText = `To find average of ${nums}:`

    bt1.addEventListener('click', function(e) {
        //Button to calculate avg
        results1.innerText = `Avg: ${y}`;
        });

/* Version 2 */////////////////////////////////////////////////////

    //Declarations

    let bt2 = document.getElementById("bt2");
    let inputs = document.getElementById("inputs");
    let num = document.getElementsByClassName("num")
    let results2 = document.getElementById("results2");
    let numCounter = 2;  // Counter for input input elements

    //Functions

    function doAvg(e) {
        let avg = 0;
        let x = 0;
        for (let i = 0; i < num.length; i++) {
            x += parseFloat(num[i].value);
        }
        avg = x / (num.length);
        console.log(x);
        results2.innerText = avg;
    };

    //Code
 
    bt2.addEventListener('click', doAvg);

    more.addEventListener('click', function(e) {
        //Dynamically builds extra input elements to average
        let newInput = document.createElement("input");
        newInput.type = "number";
        newInput.placeholder = `number ${numCounter +=1}`;
        newInput.classList.add("num");

        inputs.appendChild(newInput);
    });

