import random

def pick6():
    ticket = []
    count = 0
    for i in range(6):
        ticket.append(random.randint(0,99))
        count = count + 1
    return ticket

def compare_tickets(winner, player):
    match = 0
    for x in range(len(winner)):
        if winner[x] == player[x]:
            match = match + 1
    return match


winner = pick6()
balance = 0
earnings = 0
plays = 100000
cost = plays * 2
while plays != 0:
    plays -= 1
    balance -= 2
    player = pick6()
    matches = compare_tickets(winner, player)
    if matches == 1:
        balance += 4
        earnings += 4
    elif matches == 2:
        balance += 7
        earnings += 7
    elif matches == 3:
        balance += 100
        earnings += 100
    elif matches == 4:
        balance += 50000
        earnings += 50000
    elif matches == 5:
        balance += 1000000
        earnings += 1000000
    elif matches == 6:
        balance += 25000000
        earnings += 25000000

print(f'After 100,000 plays, your balance is ${balance}')
roi = (earnings - cost) / cost
print(f'Your return on investment is {roi:.2f}')
    

