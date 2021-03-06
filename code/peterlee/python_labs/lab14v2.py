import random

#function that selects 6 random numbers from 1-99
def pick6():
    random_set = []
    for i in range(6):
        random_set.append(random.randint(1,99))
    return random_set

#function that compares each ticket to the winning ticket
def num_matches(ticket, winning):
    match_counter = 0
    for x in range(6):
        if ticket[x] == winning[x]:
            match_counter += 1
    return match_counter

def main():
    #chooses a random winning set of numbers
    winning = pick6()
    current_balance = 0
    current_tickets = 0
    #generates 100,000 tickets while adjusting the current balance appropriately
    while current_tickets < 100001:
        ticket = pick6()
        current_tickets += 1
        current_balance -= 2
        ticket_results = num_matches(ticket, winning)
        if ticket_results == 1:
            current_balance += 4
        elif ticket_results == 2:
            current_balance += 7
        elif ticket_results == 3:
            current_balance += 100
        elif ticket_results == 4:
            current_balance += 50000
        elif ticket_results == 5:
            current_balance += 1000000
        elif ticket_results == 6:
            current_balance +=25000000

    
    print(f'Your current balance is ${current_balance}')
    expenses = 200000
    earnings = expenses + current_balance
    roi = (earnings - expenses)/expenses
    print('Your expenses are $200,000')
    print(f'Your earnings are ${earnings}')
    print(f'Your return on investment is {roi}')

main()