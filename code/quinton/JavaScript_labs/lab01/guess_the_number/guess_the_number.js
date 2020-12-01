let number = Math.floor(Math.random() * 100)

let game = true
let count = 0

while (game) {
    let guess = prompt('Guess the number between 1-100')
    if (guess < number) {
        alert('too low')
        count ++
    } else if (guess > number) {
        alert('too high')
        count ++
    } else {
        count ++
        alert(`Yup. and it only took you ${count} tries`);
        game = false
    }

}












/*
import random

game = True
number = random.randint(1, 100)
count = 0
print('Guess the number between 1-100')

while game:
    guess = int(input('Enter guess: '))
    if guess > number:
        print('Too high')
        count += 1
    elif guess < number:
        print('Too low')
        count += 1
    else:
        count += 1
        print(f'Yup. It took you {count} tries')
        game = False
*/