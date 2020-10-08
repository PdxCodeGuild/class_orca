'''
PDX Code Guild
Daniel Eggimann
Lab 14 Version 1
'''

# imports
import random

def pick6():
    six_nums = []
    counter = 0
    while counter <=5:
        counter += 1
        six_nums.append((random.randint(1, 99)))
    return six_nums

winning_nums = pick6()

def compare_tix(comp, gambler):
    matching_nums = 0
    counter = 0
    for num in comp:
        if comp[counter] == gambler[counter]:
            matching_nums += 1
            counter += 1
        else:
            counter += 1        
    return matching_nums

def winning_total(matches):
    if matches == 0:
        return 0
    elif matches == 1:
        return 1
    elif matches == 2:
       return 7
    elif matches == 3:
       return 100
    elif matches == 4:
        return 50000
    elif matches == 5:
        return 1000000
    elif matches == 6:
        return 25000000
        
def main():
    # net winnings for gambler
    net_winnings = 0
    float(net_winnings)
    counter = 0
    while counter <= 100000:
        # cost of a ticket
        net_winnings -= 2
        counter += 1
        gambler_nums = pick6()
        matching_nums = compare_tix(winning_nums, gambler_nums)
        winnings = winning_total(matching_nums)
        net_winnings += winnings
    # print(net_winnings)
    print(f'Your net winnings are: ${net_winnings:,.2f}')
    print('Invest in something else.')
   
main()