import datetime
dt = datetime.datetime.now()
x = dt.strftime("%m-%d-%Y %H:%M:%S")

class Account:
    def __init__(self, balance=0):
        self.balance = balance
        self.transactions = []

    def check_balance(self):
        self.transactions.append(f'Checked current balance at {x}')
        return self.balance

    def make_deposit(self, amount):
        self.balance += amount
        self.transactions.append(f'You deposited ${amount} into your account at {x}')
        print(f'\n\nYou have deposited ${amount}.  Your new balance is ${self.balance}.\n\n')
        # main_menu()
        

    def make_withdrawal(self, amount):
        if self.check_withdrawal(amount) == True:
            self.balance -= amount
            self.transactions.append(f'You withdrew ${amount} from your account at {x}')
            print(f'\n\nYou have withdrawn ${amount} from your account.  Your new balance is ${self.balance}\n\n')
        elif self.check_withdrawal(amount) == False:
            self.transactions.append(f'Your transaction was unable to be processed due to insufficient funds at {x}.')
            print(f'\n\nInsufficient funds!  You currently have {self.balance} in your account.\n\n')
        # main_menu()

    def check_withdrawal(self, amount):
        if self.balance >= amount:
            return True
        else:
            return False

    def transaction_history(self):
        for i in self.transactions:
            print(f'{i}\n')
        # main_menu()
    
# def main_menu():
#     main_menu = input('Would you like to go back to the main menu?  Enter y for yes and n for quit:\n>')
#     if main_menu == 'y':
#         main()
#     elif main_menu == 'n':
#         quit()



# def main():
ATM = Account(0)
while True:
    user_input = int(input('''Welcome tp the ATM!  Please input your selection from the following list:
    1) Check your balance
    2) Make a deposit
    3) Make a withdrawal
    4) View your transaction history
    5) Exit ATM
    '''))

    if user_input == 1:
        print(f'\n\nYour current balance is ${ATM.check_balance()}\n\n')
        # main_menu()
    elif user_input == 2:
        amount = int(input('What is the amount you would like to deposit?\n'))
        ATM.make_deposit(amount)

    elif user_input == 3:
        amount = int(input('How much would you like to withdraw from your account?\n'))
        ATM.make_withdrawal(amount)

    elif user_input == 4:
        ATM.transaction_history()

    elif user_input == 5:
        quit()
    else:
        print('\n\nInvalid selection!\n\n')
    
    








# main()


