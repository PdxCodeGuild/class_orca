# LAB 20 - Credit Card Validation
# obtaining user's CC number
user_card = input('Enter in your 16-digit credit card number to validate:\n>')

# ensuring corrent amount of digits entered
if len(user_card) != 16:
    print('Please enter in a valid 16-digit credit card number!')
    user_card = input('Enter in your 16-digit credit card number to validate:\n>')

# converting to list
user_card = list(user_card)
# converting list to int
for i in range(len(user_card)):
    user_card[i] = int(user_card[i])

# obtaining check digit
check_digit = user_card.pop(-1)

# reversing list
user_card = user_card[::-1]

# doubling every other
for i in range(0, len(user_card), 2):
    user_card[i] *= 2

# subtract 9 if number over 9
user_card = [x - 9 if x > 9 else x for x in user_card]

# adding total of numbers
user_card = sum(user_card)

# ensuring check digit matches
if check_digit == user_card % 10:
    print('Valid!')
else:
    print('Invalid!')