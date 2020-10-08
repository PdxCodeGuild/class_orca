# dictionary of card possibilities
list = {
    'A': 1, '2': 2, '3': 3, '4': 4,
    '5': 5, '6': 6, '7': 7, '8': 8,
    '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10
}
# getting the inputs from the user
first_card = input('What is your first card?\n>')
second_card = input('What is your second card?\n>')
third_card = input('What is your third card?\n>')

# converting the cards to points
def convert_card_to_points(blah):
    for key in list:
        if blah == key:
            return list[key]
# adding total points
total = convert_card_to_points(first_card) + \
convert_card_to_points(second_card) + convert_card_to_points(third_card)
print(total)
# if else loop to determine the advice
if total < 17:
    print('Hit!')
elif 17 <= total < 21:
    print('Stay')
elif total == 21:
    print('Blackjack!')
else:
    print('Already Busted')