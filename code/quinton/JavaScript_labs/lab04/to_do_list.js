let user_input = document.getElementById('user_input');
let add_button = document.getElementById('add_button');
let to_do_items = document.getElementById('to_do_items'); 
let done_items = document.getElementById('done_items');



add_button.addEventListener('click', function () {
    let done_button = document.createElement('button');
            done_button.innerText = 'Done';
            done_button.value = user_input.value
            done_button.onclick = function(e) {
                to_do_items.removeChild(li);
                to_do_items.removeChild(done_button);
                to_do_items.removeChild(delete_button);
                done_items.appendChild(li);
            }
        let delete_button = document.createElement('button');
            delete_button.innerText = 'Delete';
            delete_button.value = user_input.value;
            delete_button.onclick = function(e) {
                to_do_items.removeChild(li);
                to_do_items.removeChild(delete_button);
                to_do_items.removeChild(done_button);
            }
        let li = document.createElement('li');
            li.setAttribute('id', user_input.value);
            li.innerText = user_input.value;
        to_do_items.appendChild(li);
        to_do_items.appendChild(done_button);
        to_do_items.appendChild(delete_button);
        user_input.value = ''
})

user_input.addEventListener('keydown', function (e) {
    if (e.key === "Enter") {
        let done_button = document.createElement('button');
            done_button.innerText = 'Done';
            done_button.value = user_input.value
            done_button.onclick = function(e) {
                to_do_items.removeChild(li);
                to_do_items.removeChild(done_button);
                to_do_items.removeChild(delete_button);
                done_items.appendChild(li);
            }
        let delete_button = document.createElement('button');
            delete_button.innerText = 'Delete';
            delete_button.value = user_input.value;
            delete_button.onclick = function(e) {
                to_do_items.removeChild(li);
                to_do_items.removeChild(delete_button);
                to_do_items.removeChild(done_button);
            }
        let li = document.createElement('li');
            li.setAttribute('id', user_input.value);
            li.innerText = user_input.value;
        to_do_items.appendChild(li);
        to_do_items.appendChild(done_button);
        to_do_items.appendChild(delete_button);
        user_input.value = ''
    }
})
