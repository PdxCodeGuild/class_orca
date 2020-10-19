# lab25 by Quinton Baseman

# creating balance property class
class BalanceProperty:
    def __init__(self, balance=0):
        self.balance = balance
        self.transaction_list = []
    # check the balance and append a message to transaction list
    def check_balance(self):
        self.transaction_list.append(f'User checked balance')
        return f'Current balance: {self.balance}'
    # deposit money into balance and append a message to transaction list
    def deposit(self, amount):
        self.balance += amount
        self.transaction_list.append(f'User deposited ${amount}')
        return f'New Balance: {self.balance}'
    # returning true or false depending on balance
    def check_withdrawal(self, amount):
        return amount <= self.balance
    # withdrawing the amount and append a message to transaction list
    def withdraw(self, amount):
        self.balance -= amount
        self.transaction_list.append(f'User withdrew ${amount}')
        return f'New Balance: {self.balance}'
    # printing the transaction list
    def print_transactions(self):
        return self.transaction_list

# setting the initial balance to zero
balance = BalanceProperty()
# main REPL
while True:
    choice = input('What would you like to do? (1. deposit, 2. withdraw, 3. check balance, 4. history, 5. quit)\n> ').lower()
    if choice == 'deposit' or choice == '1':
        amount = int(input('How much would you like to deposit?\n> '))
        print(balance.deposit(amount))
    elif choice == 'withdraw' or choice == '2':
        amount = int(input('How much would you like to withdraw?\n> '))
        if balance.check_withdrawal(amount):
            balance.print_transactions()
            print(balance.withdraw(amount))
        else:
            print('Insufficiant funds.')
    elif choice == 'check balance' or choice == '3':
        print(balance.check_balance())
    elif choice == 'history' or choice == '4':
        print(balance.print_transactions())
    elif choice == 'quit' or choice == '5':
        break