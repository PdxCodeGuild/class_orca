
# *'-.-'*'-.-'*'-.-'*-.-'*-.-'*-.-'*-.-'*'-.-'*'-.-'*'-.-'*
#        Project: Python
# Assignment/Ver: Lab25
#         Author: Ron Mansolilli, ron.mansolilli@gmail.com
#           Date: 10-15-2020
# *'-.-'*'-.-'*'-.-'*-.-'*-.-'*-.-'*-.-'*'-.-'*'-.-'*'-.-'*

#----Instructions and notes-----------------------------------------
''' 

Lab 25: ATM

'''
#----Modules--------------------------------------------------------

import string
import math

#----Classes--------------------------------------------------------

class Account:
    def __init__(self, x, name, deposit=0, withdraw=0, transactions=[]):
        self.balance = x
        self.name = name
        self.deposit = deposit
        self.withdraw = withdraw
        self.transactions = transactions
# above:  You can set all the variables to private to block calls on variable 
#   outside of the class i.e. self.__balance

    def check_balance(self): 
        print(f"\nYour balance is ${self.balance}")

# Above: do not just print (not good?), just return a value and then print
    
    def deposit_amount(self, amt):
        self.balance += amt
        self.transactions.append(f'User deposited ${amt}')
# Above: would have been interesting to add balance as well in list

    def __check_withdraw(self, amt):
        if amt <= self.balance:
            return True
# Above: you can also return False in an else statement
# Also, even better just return = amt <= self.balance

    def withdrawal(self, amt):
        if self.__check_withdraw(amt) is True:
            self.balance -= amt
            self.transactions.append(f'User withdrew ${amt}')
        else:
            print('\nInsufficient Funds (i.e. "no money, no cry")')
            print(f'You only have ${self.balance}. Please try again...\n')
            main()
# above:  instead of printing outside of main - raise an error instead. 
#  in this case: raise ValueError("not enough money in account")

    def print_transactions(self):
        print('\nTransaction History')
        print('-------------------')
        for x in range(len(self.transactions)):
            print(self.transactions[x])
# different for loop:  for trans in self.transactions:
#                         print(trans)
# OR:  print("\n".join(self.__transactions))

#----Functions--------------------------------------------------

def choices():#-------------------------------------------
    '''In or Out options'''

    while True:
        yn = input(f'\nWould you like to return to the main menu (y/n): ')
        if yn == 'y':
            main()
        elif yn == 'n':
            print('\n\t** Goodbye **\n')
            exit()
        else:
            print('invalid selection')
            continue

#----Main----------------------------------------------------------

u1 = Account(0,"Ron")

def main():

    ''' Welcome screen and interface '''

    print('''   
    ***** Welcome to Ron's Bank! *****
  "We love your money, like it's our own"

Please select from the following options:

           1. Check Balance
           2. Withdraw
           3. Deposit
           4. History
           or 'exit'   
''')

    # User menu logic
    choice = ''
    while choice != ('1', '2', '3', '4', 'exit'):
        choice = input('\t>>> ')
        if choice == '1':
            u1.check_balance()
            choices()                 
        elif choice == '2':
            u1.withdrawal(int(input("\nHow much would you like to withdraw: ")))
            print(f'\nYour new balance is: ${u1.balance}')
            choices()
# above:  you can use a try: / except: function under line 113 and then add a fee, etc.
# the except will return an error of you choice (i.e. ValueError) and return stuff
        elif choice == '3':
            u1.deposit_amount(int(input("\nHow much would you like to deposit: ")))
            print(f'\nYour new balance is: ${u1.balance}')
            choices()
        elif choice == '4':
            u1.print_transactions()
            choices()             
        elif choice == 'exit':
            quit()                  
        else:
            print('\n>>> Invalid selection, try again:\n')
            continue
    
main()



