
# dictionary assigning values to cards
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

# input asks for cards user has
card_1 = input("What is your first card? ")
card_2 = input("What is your second card? ")
card_3 = input("What is your third card? ")

ace_check = [card_1, card_2, card_3]
for a in ace_check:
    if a == 'A':
        ace_value = 0
        for 'A' in ace_check:
            ace value += 10

if ace_value = True:
    total_value = values[card_1] + values[card_2] + values[card_3] + ace_check
else:
    total_value = values[card_1] + values[card_2] + values[card_3]


# checks the total value against some comparisons to determine best advice
if total_value < 17:
    action = 'You should hit.'
elif 17 <= total_value <= 21:
    action = 'You should stay.'
elif total_value == 21:
    action = 'You got Blackjack!'
else:
    action = 'You\'re already busted'

# prints out the total value and advice
print (f"Your total value is {total_value}. {action}")
