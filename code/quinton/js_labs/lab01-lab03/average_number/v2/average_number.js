let number_list = []
let add_button = document.getElementById('add');
let finish_button = document.getElementById('finish');
let user_input = document.getElementById('user_input');
let average = document.getElementById('average');
let array = document.getElementById('array');
let total = 0

function addToList(e) {
    number_list.push(' ' + parseInt(user_input.value));
    array.innerText = number_list
    user_input.value = '';
}
add_button.addEventListener('click', addToList);


user_input.addEventListener('keydown', function(e) {
    if (e.key === "Enter") {
        addToList(user_input);
    }
});
finish_button.addEventListener('click', function() {
    for (let i=0; i<number_list.length; i++) {
        if (number_list[i]) {
            total += parseFloat(number_list[i])
        }
    }
    let average_of_all_numbers = total / number_list.length;
    average.innerText = `The average of the above list of numbers is ${average_of_all_numbers}`
});


