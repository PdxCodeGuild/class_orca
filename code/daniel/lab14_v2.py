'''
PDX Code Guild
Daniel Eggimann
Lab 14 Version 1
'''

# imports
import random

def pick6():
    '''Generates 6 random numbers and returns those numbers.'''
    # six_nums = []
    
    # for x in range(6):
    #     six_nums.append((random.randint(1, 99)))
    # return six_nums
    return [random.randint(1,99) for x in range(6)]

winning_nums = pick6()

def compare_tix(comp, gambler):
    '''Calls the winning and gambler numbers to compare 
    and returns to total number of matches'''
    matching_nums = 0
    # counter = 0
    # for num in comp:
    #     if comp[counter] == gambler[counter]:
    #         matching_nums += 1
    #         counter += 1
    #     else:
    #         counter += 1 
    for win, tix in zip(comp, gambler):
        if win == tix:
            matching_nums += 1           
    return matching_nums

def winning_total(matches):
    '''Calls the quantity of matching numbers to the amount won'''
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
    '''Runs a loop n times and returns total winnings'''
    # net winnings for gambler
    net_winnings = 0
    float(net_winnings)
    # loop for gambler to play
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
    roi = net_winnings/(counter*2)
    print(f'Your return on investment ratio is: {roi:.2f}')
    print('You should invest in something else.')

main()