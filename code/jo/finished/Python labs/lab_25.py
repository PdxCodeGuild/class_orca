
# defines a class
class Balance:
    # initializes the starting balance(b) and sets it to 0. also makes empty transactions list
    def __init__(self,b=0):
        self.b = b
        self.transactions = []

    # checks the balance
    def check_balance(self):
        return self.b

    # adds an entered amount to the balance. also adds the amount to the transactions list
    def deposit(self, a):
        self.b += a
        self.transactions.append(f'deposited {a}')
        return self.b

    # checks to see if the entered amount is greater than the total in the balance
    def check_withdrawl(self, a):
        if self.b >= a:
        #     return True
        # if self.b <= a:
        #     return False

    # subtracts an entered amount. also adds to transaction list
    def withdraw(self, a):
        self.b -= a
        self.transactions.append(f'withdrew {a}')
        return self.b

    # prints the transactions
    def print_transactions(self):
        print(transactions )

# saves the class to a variable name to use with methods later
accnt = Balance()

# REPL
while True:
    # asks user what action they would like to do
    action = input("""What would you like to do?\nType 'v' to view account balance.\nType 'd' to make a deposit.\nType 'w' to make a withdrawl.\nType 't' to view transactions.\nType 'e' to print balance and exit. 
""")
    # displays the balance
    if action == 'v':
        print(f'Your account balance is ${accnt.check_balance()}\n')

    # user sets an amount to deposit. that number is saved as a variable to be called by the class.method
    elif action == 'd':
        d_amount = int(input("How much would you like to deposit? "))
        print(f'You deposited ${accnt.deposit(d_amount)}\n')

    # user sets an amount to withdraw. number is saved to variable to be called. check_withdraw compares it to balance to make sure that amount is available
    elif action == 'w':
        w_amount = int(input("How much would you like to withdraw? "))
        while accnt.check_withdrawl(w_amount) is False:
            print(f'You cannot withdraw ${w_amount}. You only have ${accnt.check_balance()} in your account. Please enter the amount you would like to withdraw.\n')
            w_amount = int(input("How much would you like to withdraw? \n"))
        else:
            accnt.withdraw(w_amount)
            print(f"You withdrew ${w_amount}. You're new total is ${accnt.check_balance()}.\n")

    # prints account transaction
    elif action == 't':
        print(f'Here are your recent transactions. {accnt.print_transactions()}\n')

    # exits
    elif action == 'e':
        print(f'Your final balance is ${accnt.check_balance()}')
        break






