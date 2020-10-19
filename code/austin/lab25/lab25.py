#Lab25 ATM

transactions = []

class Bank_Account:

    def __init__(self):
        self.balance = 0

    def check_balance(self):
        print(self.balance)
        return self.balance

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f'Current balance: {self.balance}')
        transactions.append(f'user deposited ${amount}')
        return self.balance
    
    def check_withdrawal(self, amount):
        if self.balance - amount >= 0:
            remaining = self.balance - amount
            print(f'Your balance would be: {remaining}')
            return True
        else:
            print("You don't have enough money")
            return False
    
    def withdraw(self, amount):
        self.balance = self.balance - amount
        print(self.balance)
        transactions.append(f'user withdrew ${amount}')
        return self.balance
    
    def print_transactions(self):
        print(transactions)


my_account = Bank_Account()

#Account REPL
while True:
    select = input("What would you like to do? Type 'deposit,' 'withdraw,' 'check balance,' 'history'  or 'done' ")
    if select == "deposit":
        amount = int(input("Amount of deposit? "))
        my_account.deposit(amount)
    elif select == "withdraw":
        amount = int(input("Amount to withdraw? "))
        my_account.withdraw(amount)
    elif select == "check balance":
        amount = int(input("Amount you want to spend? "))
        my_account.check_withdrawal(amount)
    elif select == "history":
        my_account.print_transactions() 
    elif select == "done":
        break
    else:
        print("Please type a valid selection")


