
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
    current_list.innerText = ''; // Reset current_list for rewrite
    for (let i = 0; i < grocery_list.length; i++) {
        //Filter by completed
        if (grocery_list[i].completed === false) {  
            let current_item = document.createElement('li');    //Create the element to be written

            let bt3_del = document.createElement('input');      //Build the delete button
            bt3_del.setAttribute('type', 'button');              //Build the delete button
            bt3_del.setAttribute('value', 'Delete');
            bt3_del.setAttribute('id', i);

            current_item.innerText = grocery_list[i].item;      //Assigns item to html list          
            current_list.append(current_item, bt3_del);         //Output: item, delete button

            bt3_del.addEventListener('click', function(e) {
                // console.log(grocery_list[bt3_del.id]);
                // console.log(bt3_del.id);
                grocery_list[bt3_del.id].completed = true;
                // console.log(grocery_list[bt3_del.id]);
                populate_list();
            });   
        };
    };
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

    //Populate the grocery list
        populate_list();
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

// Buttons and Events

    bt1_add.addEventListener('click', function(e) {
        //Button to add items to current list
        console.log(current_list.value)
        current_list.innerText = '';    // Reset current_list for rewrite
        grocery_list.push({"item" : items.value, "completed" : false,});

        //Populate the grocery list
        populate_list(); 
        items.value = ''; // Reset input box
    });

// End code

