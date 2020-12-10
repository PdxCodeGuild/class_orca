
//  *'-.-'*'-.-'*'-.-'*-.-'*-.-'*-.-'*-.-'*'-.-'*'-.-'*'-.-'*
//         Project: Javascript
//  Assignment/Ver: Lab 4
//          Author: Ron Mansolilli, ron.mansolilli@gmail.com
//            Date: 12-7-2020
//  *'-.-'*'-.-'*'-.-'*-.-'*-.-'*-.-'*-.-'*'-.-'*'-.-'*'-.-'*

// ----Instructions and notes--------------------------------

    /* Grocery List */

// ----Global variables, arrays, etc. ------------------

let grocery_list = [
    { "item" : "Lettuce", "completed" : false, },
    { "item" : "coffee", "completed" : false, },
    { "item" : "bread", "completed" : false, },
    { "item" : "cereal", "completed" : true, },
    { "item" : "tomatoes", "completed" : true, },
]
 
// ----Functions----------------------------------------------

function populate_list() {

    

};



// ----Main Code---------------------------------------------

// Declarations

    let items = document.getElementById('items');
    let bt1_add = document.getElementById('bt1_add');
    let bt2_update = document.getElementById('bt2_update');
    let current_list = document.getElementById('current_list');
    let deleted_list = document.getElementById('deleted_list');

// Code

    if (grocery_list === undefined || grocery_list.length == 0) {
        //Check to see if empty
        current_list.innerText = "No items to show";
    } else {
        //Populate the current list
        for (let i = 0; i < grocery_list.length; i++) {
            //Filter by completed
            if (grocery_list[i].completed === false) {  
                let current_item = document.createElement('li');    //Create the element to be written

                let bt3_del = document.createElement('input');      //Build the delete button
                bt3_del.setAttribute('type', 'button');              //Build the delete button
                bt3_del.setAttribute('value', 'Delete');
                bt3_del.setAttribute('id', i);


                current_item.innerText = grocery_list[i].item;      //Assigns item to html list

                // listElement.append(listItem,listItemCheckbox,listItemLabel,editButton,deleteButton);
                // current_list.innerHTML+= listItemCheckbox.outerHTML + listItemLabel.outerHTML + editButton.outerHTML + deleteButton.outerHTML;
                
                current_list.append(current_item, bt3_del);         //Output: item, delete button
                // current_list.appendChild(current_item);
                // current_list.appendChild(bt3_del);
 
                bt3_del.addEventListener('click', function(e) {
                    console.log(grocery_list[bt3_del.id]);
                    console.log(bt3_del.id);
                    grocery_list[bt3_del.id].completed = true;
                    console.log(grocery_list[bt3_del.id]);

                }); 

                
            };
        };
        //Populate the deleted list
        for (let i = 0; i < grocery_list.length; i++) {
            //Filter by uncompleted
            if (grocery_list[i].completed === true) {  
                let current_item = document.createElement('li');
                current_item.innerHTML = grocery_list[i].item;
                deleted_list.appendChild(current_item);
            };
        };
    };

// Buttons and Events

    bt1_add.addEventListener('click', function(e) {
        //Button to add items to current list
        console.log(current_list.value)
        current_list.innerText = ''; // Reset current_list for rewrite
        grocery_list.push({"item" : items.value, "completed" : false,});

        for (let i = 0; i < grocery_list.length; i++) {
            //Build current list with new item
            if (grocery_list[i].completed === false) {
                let current_item = document.createElement('li');
                current_item.innerText = grocery_list[i].item;
                current_list.appendChild(current_item);
            };
        };  
      items.value = ''; // Reset input box
    });

// End code

  






// bt1_update.onclick = function() {
//     // Button
//     current_list.innerText = 'test';

// };


//     // Declarations

//     let card = document.getElementsByClassName("card");
//     let inputs = document.getElementById("inputs");
//     let bt2 = document.getElementById("bt2");
//     let bt1 = document.getElementById("bt1");
//     let results = document.getElementById("results")
//     let add = 0;

// // Code

//     bt2.addEventListener('click', function() {
//         // Button
//         console.log(card[0].value);
//         add = sum();
//         // console.log(add);
//         let recommendation = hand_eval(add);
//         results.innerText = recommendation;
//         // console.log(recommendation);
//     });



// function check_jqka(cc) {
//     //Check for Jack/Queen/King/Ace and change values appropriately
//     // console.log("Made it to check jqka")
//     // console.log(cc)
//     if (cc === ("j") || cc === ("q") || cc === ("k")) {
//         cc = 10;
//         // console.log("needs a 10")
//     } else if (cc === "a") {
//         cc = 11;
//     };
//     // console.log(cc)
//     return cc;
// };

// function sum() {
//     //Function to Sum array of numbers
//     let tally = 0;
//     for (let i = 0; i < card.length; ++i) {
//         // console.log(card[i].value)
//         card[i].value = check_jqka(card[i].value);
//         // console.log(card[i].value)
//         tally += parseFloat(card[i].value);
//     };
//     return tally
// };

// function hand_eval(x1) {
//     //Hand evaluation function
//     if (x1 < 17) {
//         return ('Hit');
//     } else if (x1 > 16 && x1 < 21) {
//         return ('Stay');
//     } else if (x1 === 21) {
//         return ('Blackjack!');
//     } else if (x1 > 21) {
//         return ('Busted');
//     } else {
//         return ('Invalid Selection');
//     };
// };

// console.log(grocery_list)

// for (i in myObj.cars) {
//     x += "<h1>" + myObj.cars[i].name + "</h1>";
//     for (j in myObj.cars[i].models) {
//       x += myObj.cars[i].models[j];
//     }
//   }
