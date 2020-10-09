import random

balance = 0
balance_debit = 0
new_balance = 0

lotto_1 = random.randint(1, 99)
lotto_2 = random.randint(1, 99)
lotto_3 = random.randint(1, 99)
lotto_4 = random.randint(1, 99)
lotto_5 = random.randint(1, 99)
lotto_6 = random.randint(1, 99)

winning_numbers = [lotto_1, lotto_2, lotto_3, lotto_4, lotto_5, lotto_6]

print(f'The winning numbers are: {lotto_1}, {lotto_2}, {lotto_3}, {lotto_4}. {lotto_5}, {lotto_6}')

def pick_6():
    score = []
    count = 0

    choice_1 = random.randint(1, 99)
    choice_2 = random.randint(1, 99)
    choice_3 = random.randint(1, 99)
    choice_4 = random.randint(1, 99)
    choice_5 = random.randint(1, 99)
    choice_6 = random.randint(1, 99)

    ticket = [choice_1, choice_2, choice_3, choice_4, choice_5, choice_6]

    for i in range(0, len(ticket), 1):
        if ticket[i] == winning_numbers[i]:
            score.append(ticket[i])
            count += 1

    return count

loop_count = 0

while loop_count < 10000:
    loop_count += 1
    count = pick_6()

    if count == 1:
        new_balance += 4
    
    if count == 2:
        new_balance += 7
    
    if count == 3:
        new_balance += 100
    
    if count == 4:
        new_balance += 50000
    
    if count == 5:
        new_balance += 1000000
    
    if count == 6:
        new_balance += 25000000

    balance_debit -= 2


earnings = balance_debit + new_balance 
roi = earnings / balance_debit
print(f'You earned {earnings} dollars')
print(f'Your return on investment was {roi}')









