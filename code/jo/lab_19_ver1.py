values = {
    "A": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "J": 10,
    "Q": 10,
    "K": 10
}

card_1 = input("What is your first card? ")
card_2 = input("What is your second card? ")
card_3 = input("What is your third card? ")

total_value = values[card_1] + values[card_2] + values[card_3]

if total_value < 17:
    action = 'You should hit.'
elif 17 <= total_value <= 21:
    action = 'You should stay.'
elif total_value == 21:
    action = 'You got Blackjack!'
else:
    action = 'You\'re already busted'

print (f"Your total value is {total_value}. {action}")