let characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()?<>{}[]'
let password = ''

num_of_characters = parseInt(prompt('How many characters would you like your password to be?'))

while (password.length < num_of_characters) {
    password += characters[Math.floor(Math.random() * characters.length)];
}

alert(`Completely randomized password with ${num_of_characters} characters: \n${password}`)