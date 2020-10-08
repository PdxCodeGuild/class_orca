import random

def pick6():
    random_set = []
    for i in range(6):
        random_set.append(random.randint(1,99))
    return random_set

winning = pick6()

def num_matches(ticket, winning=winning):
    match_counter = 0
    for x in range(6):
        if ticket[x] == winning[x]:
            match_counter += 1
    return match_counter

def main():
    current_balance = 0
    current_tickets = 0
    while current_tickets < 100001:
        ticket = pick6()
        current_tickets += 1
        ticket_results = num_matches(ticket)
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
        else:
            current_balance -= 2
    

    print(current_balance)



main()