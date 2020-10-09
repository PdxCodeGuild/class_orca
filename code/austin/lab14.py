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

    print(ticket)

    for i in range(0, len(ticket), 1):
        for j in range(0, len(winning_numbers), 1):
            if ticket[i] == winning_numbers[j]:
                score.append(ticket[i])
                count += 1

    print(f'You matched {count} numbers!') 
    return count

loop_count = 0

while loop_count < 10000:
    loop_count += 1
    count = pick_6()
    print(new_balance, "this is new balance")

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

print(balance_debit)
print(new_balance, "gross winnings")

earnings = balance_debit + new_balance 
roi = earnings / balance_debit
print(f'You earned {earnings} dollars')
print(f'Your return on investment was {roi}')




# def get_balance(pick_6, balance, balance_debit):
#     for _ in range(100):
#         pick_6()
#         balance_debit -= 2
#         # balance += x
#         print(balance_debit)
#         print(balance, "this is x")
    








