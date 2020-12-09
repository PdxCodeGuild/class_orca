
//get our elements from the page
const div_container = document.getElementById('container');
const div_new_items = document.getElementById('new_items');
const div_completed_items = document.getElementById('completed_items');
const button_add_new = document.getElementById('button_add_new');
let field_new_task = document.getElementById('field_new_task');
let task_ID_counter = 1111

button_add_new.addEventListener ('click', function(click) {
    add_task(field_new_task.value);
});

field_new_task.addEventListener('keydown', function(enterkey) {
    if ( enterkey.key === "Enter" ) {
        add_task(field_new_task.value);
    };
});

// run this each time new task is added
function add_task(task_name) {
    // create all the HTML:
    let new_task_div = document.createElement('div');
    new_task_div.className = task_ID_counter;
    let new_task_checkbox = document.createElement('input');
    new_task_checkbox.className = task_ID_counter;
    new_task_checkbox.type = 'checkbox';
    new_task_checkbox.addEventListener('click', function(checkbox_click) {
        swap_completed(new_task_checkbox.className);
    });
    let new_task_label = document.createElement('label');
    new_task_label.className = task_ID_counter;
    new_task_label.for = task_ID_counter;
    new_task_label.innerText = ' <<< Mark complete || Task : ' + task_name + ' || Permanently delete >>> ';
    let delete_checkbox = document.createElement('input');
    delete_checkbox.className = task_ID_counter;
    delete_checkbox.type = 'checkbox';
    delete_checkbox.addEventListener('click', function(checkbox_click) {
        delete_task(delete_checkbox.className);
    });
    let new_br = document.createElement('br');
    new_br.className = task_ID_counter;
    //

    task_ID_counter++; // agument id counter

    // add all the items to the page -- first add the div for the task, then add all the elements INSIDE that div
    div_new_items.appendChild(new_task_div);
    new_task_div.appendChild(new_task_checkbox);
    new_task_div.appendChild(new_task_label);
    new_task_div.appendChild(delete_checkbox);
    new_task_div.appendChild(new_br);
};

//run this each time main checkbox is selected, checking value and alternating between completed or not
function swap_completed(task_id) {
    console.log(`swap_completed running with input task_id: ${task_id}`);
    all_id_elements = document.getElementsByClassName(task_id);
    console.log(`all_id_elements[1].checked : ${all_id_elements[1].checked} and all_id_elements.length : ${all_id_elements.length}`);
    console.log(`all_id_elements[0] is ${all_id_elements[0]}`); // [0] is [object HTMLDivElement]
    console.log(`all_id_elements[1] is ${all_id_elements[1]}`); // [1] is [object HTMLInputElement]
    console.log(`all_id_elements[2] is ${all_id_elements[2]}`); // [2] is [object HTMLLabelElement]
    console.log(`all_id_elements[3] is ${all_id_elements[3]}`); // [3] is [object HTMLInputElement]
    console.log(`all_id_elements[4] is ${all_id_elements[4]}`); // [4] is [object HTMLBRElement]

    if (all_id_elements[1].checked === true) {
        div_completed_items.appendChild(all_id_elements[0]);
        all_id_elements[2].style = "text-decoration: line-through";
        datetime = new Date();
        console.log(datetime);
    }
    else if ( all_id_elements[1].checked === false) {
        div_new_items.appendChild(all_id_elements[0]);
        all_id_elements[2].style = "";
    };
    
};

// delete checkbox function
function delete_task(task_id) {
    console.log(`delete_task running with input task_id: ${task_id} and task name: `);
    all_id_elements = document.getElementsByClassName(task_id);
    all_id_elements[0].remove();
};


// var minutes = 1000 * 60;
// var hours = minutes * 60;
// var days = hours * 24;
// var years = days * 365;
// var d = new Date();
// var t = d.getTime();
// var y = Math.round(t / years); 

// / / / / / / / / / / / / / / / / / 
// misc. notes:
// p_text.setattribute('id', samething.value);
// JAVASCRIPT LINTER NAME: LF, JAVASCRIPT STANDARD STYLE, PRETTIER

// / / / / / / / / / / / / / / / / / 
// HTML IDs USED:

// div id='container'
// button id="button_add_new"
// input id="field_new_task"
// div id='new_items'
// div id='completed_items'
// / / / / / / / / / / / / / / / / /

// ##############################################################################
// # John Fial, PDX Code Guild, 2020-2021, www,johnfial.com
// https://github.com/PdxCodeGuild/class_orca/blob/main/4%20JavaScript/labs/lab04-todo.md
// ##############################################################################
