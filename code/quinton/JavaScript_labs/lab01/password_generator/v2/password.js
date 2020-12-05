let characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*?';
let password = '';
let num_of_characters = document.getElementById('num_of_characters');
let generate = document.getElementById('generate');
let your_password = document.getElementById('your_password');

generate.addEventListener('click', function() {
    while (password.length < parseInt(num_of_characters.value)) {
        password += characters[Math.floor(Math.random() * characters.length)];
    }
    your_password.innerText = `Your random password with ${num_of_characters.value} characters: ${password}`;
    num_of_characters.value = '';
})

num_of_characters.addEventListener('keydown', function(e) {
    if (e.key === "Enter") {
        while (password.length < parseInt(num_of_characters.value)) {
            password += characters[Math.floor(Math.random() * characters.length)];
        }
        your_password.innerText = `Your random password with ${num_of_characters.value} characters: ${password}`;
        num_of_characters.value = '';
}})