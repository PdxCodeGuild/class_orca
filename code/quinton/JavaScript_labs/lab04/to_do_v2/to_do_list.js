let add_button = document.getElementById('add_button');
let user_input = document.getElementById('user_input');
let to_do_items = document.getElementById('to_do_items');
// let done_button = document.getElementById('done_button');
let delete_button = document.getElementById('delete_button');
let to_do = document.getElementById('to_do');
let done_items = document.getElementById('done_items');
let done = document.getElementById('done');






add_button.addEventListener('click', function() {
  let br = document.createElement('br');
  let check_box = document.createElement('input');
  check_box.setAttribute('type', 'checkbox');
  check_box.setAttribute('name', user_input.value);
  check_box.setAttribute('value', user_input.value);
  check_box.setAttribute('id', 'check_box');
  let new_item = document.createElement('label');
  new_item.setAttribute('for', check_box.value);
  new_item.innerText = user_input.value;
    to_do_items.appendChild(check_box);
    to_do_items.appendChild(new_item);
    to_do_items.appendChild(br);
    user_input.value = '';
    to_do.addEventListener('submit', function(e) {
      e.preventDefault();
      if (check_box.checked === true) {
        done_items.appendChild(check_box);
        done_items.appendChild(new_item);
        done_items.appendChild(br);
        check_box.checked = false;
      }
    done.addEventListener('submit', function(e) {
      e.preventDefault();
      if (check_box.checked === true) {
        done_items.removeChild(check_box);
        done_items.removeChild(new_item);
        done_items.removeChild(br);
      }
    }) 
    })
  })

user_input.addEventListener('keydown', function(e) {
  if (e.key === 'Enter') {
    let br = document.createElement('br');
  let check_box = document.createElement('input');
  check_box.setAttribute('type', 'checkbox');
  check_box.setAttribute('name', user_input.value);
  check_box.setAttribute('value', user_input.value);
  check_box.setAttribute('id', 'check_box');
  let new_item = document.createElement('label');
  new_item.setAttribute('for', check_box.value);
  new_item.innerText = user_input.value;
    to_do_items.appendChild(check_box);
    to_do_items.appendChild(new_item);
    to_do_items.appendChild(br);
    user_input.value = '';
    to_do.addEventListener('submit', function(e) {
      e.preventDefault();
      if (check_box.checked === true) {
        done_items.appendChild(check_box);
        done_items.appendChild(new_item);
        done_items.appendChild(br);
        check_box.checked = false;
      }
    done.addEventListener('submit', function(e) {
      e.preventDefault();
      if (check_box.checked === true) {
        done_items.removeChild(check_box);
        done_items.removeChild(new_item);
        done_items.removeChild(br);
      }
    }) 
    })
  }})