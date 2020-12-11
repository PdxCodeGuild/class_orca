let input = document.getElementById('input');
let button = document.getElementById('button');
let hint = document.getElementById('hint');

let secret_number = Math.floor(Math.random() * 100);
let count = 0;

button.addEventListener('click', function() {
    if (parseInt(input.value) < secret_number) {
        count ++;
        hint.innerText = 'Too Low';
        input.value = ''
    } else if (parseInt(input.value) > secret_number) {
        count ++;
        hint.innerText = 'Too high';
        input.value = ''
    } else {
        count ++;
        hint.innerText = `You got it! It took you ${count} tries.`
    }})

input.addEventListener('keydown', function(e) {
    if (e.key === "Enter") {
        if (parseInt(input.value) < secret_number) {
            count ++;
            hint.innerText = 'Too Low';
            input.value = ''
        } else if (parseInt(input.value) > secret_number) {
            count ++;
            hint.innerText = 'Too high';
            input.value = ''
        } else {
            count ++;
            hint.innerText = `You got it! It took you ${count} tries.`
        }}
});
