# This is Lab 14 Ver 1, The pick 6 problem

def main():
    
    def rand_pick(nums = 6):
        import random
        ticket = []
        for num in range(0,nums):
            new_num = random.randint(1,99) 
            ticket.append(new_num)
        return ticket
    def matching_num(winning_ticket, my_ticket):
        matching_numbers = 0
        for i in range(0,6):
            if my_ticket[i] == winning_ticket[i]:
                matching_numbers += 1
        return matching_numbers
    
    

    lets_play = input("You have $200,000. Do you want to blow it on lottery tickets?:\n 'y' or 'n'?\n")
    while lets_play != 'y' and lets_play != 'n':
        lets_play = input("\n 'y' or 'n'?")
        
    if lets_play == "n":
        print("Ahhhh. Are You yellow?")
        return

    if lets_play == "y":
   
        winnings = {0:0, 1:4, 2:7, 3:100, 4:50000, 5:1000000, 6:25000000}
        bankroll = 200000
        total_winnings = 0
        # expenses = 0
        winning_ticket = rand_pick()
        
        print(winning_ticket)
        while bankroll > 0:
            my_ticket = rand_pick()
            print(f'''The winning ticket is{winning_ticket},
            your ticket is:{my_ticket}\n''')
            winning_numbers = matching_num(winning_ticket, my_ticket)
            print (f"You have {winning_numbers} matching numbers you win ${winnings[winning_numbers]}")
            total_winnings += winnings[winning_numbers]
            print (f"\nYour total winnings are ${total_winnings}!")
            bankroll -= 2
            # expenses += 2
            # roi_percent = ()
        
        print(f'''You blew your load on lottery tickets.
        You won ${total_winnings}!
        Your mom and dad are proud!''')
main()