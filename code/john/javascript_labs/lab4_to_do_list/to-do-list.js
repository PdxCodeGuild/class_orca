// ##############################################################################
// # John Fial, PDX Code Guild, 2020-2021, www,johnfial.com
// https://github.com/PdxCodeGuild/class_orca/blob/main/4%20JavaScript/labs/lab04-todo.md
// Let's make a simple todo-list which supports the following operations:
    //     add an item to the list
    //     remove an item from the list
    //     mark an item as completed
    //     Removed items should disappear entirely. Completed items should appear at the bottom (or in a separate list) with a line through them.
// ##############################################################################

// / / / / / / / / / / / / / / / / / HTML IDs USED:
// div id='container'

// button id="button_add_new"
// input id="field_new_task"

// div id='new_items'
// div id='completed_items'
// / / / / / / / / / / / / / / / / /

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

function add_task(task_name) {
    
    // create all the HTML:
    let new_task_div = document.createElement('div');
    new_task_div.class = task_ID_counter;
    let new_task_checkbox = document.createElement('input');
    new_task_checkbox.class = task_ID_counter;
    new_task_checkbox.type = 'checkbox';
    new_task_checkbox.addEventListener('click', function(checkbox_click) {
        swap_completed(new_task_checkbox.class);
    });
    let new_task_label = document.createElement('label');
    new_task_label.class = task_ID_counter;
    new_task_label.for = task_ID_counter;
    new_task_label.innerText = task_name;
    let new_br = document.createElement('br');
    new_br.class = task_ID_counter;
    
    //increase the ID counter
    task_ID_counter++; 

    div_new_items.appendChild(new_task_div);
    new_task_div.appendChild(new_task_checkbox);
    new_task_div.appendChild(new_task_label);
    new_task_div.appendChild(new_br);
};

function swap_completed(task_id) {
    console.log(`swap_completed running with input task_id: ${task_id}`);
    // console.log(`clicked new_task_checkbox.id is # think this is a BS value: #  ${new_task_checkbox.id}`);
    // console.log(`clicked new_task_checkbox.checked is # think this is a BS value: #  ${new_task_checkbox.checked}`);
    all_id_elements = document.getElementsByClassName(task_id)
    console.log(all_id_elements);
    
};


function delete_task(task_id) {pass};

// p_text.setattribute('id', samething.value);




// JAVASCRIPT LINTER NAME: LF, JAVASCRIPT STANDARD STYLE, PRETTIER