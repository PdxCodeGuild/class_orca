let number_list = []

let game = true
let total = 0

while (game) {
    let choice = prompt("Enter a number, or 'done'");
    if (choice == 'done') {
        game = false;
    } else {
        number_list.push(parseInt(choice));
    }
}

number_list.forEach(function(number) {
    total += number
});

alert(`Your number list: [${number_list}] \nThe average number: ${total/number_list.length}`)

