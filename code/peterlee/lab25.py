class account:

    def __init__(self):
        self.balance = 0
        self.list = []

    def check_balance(self):
        return self.balance
    
    def deposit(self, deposit_amount):
        self.balance += deposit_amount
        self.list.append(f'User deposited {deposit_amount}.')
        return self.balance

    def check_withdrawal(self, check_withdrawal_amount):
        if check_withdrawal_amount > self.balance:
            return False
        else:
            return True
    
    def withdraw(self, withdrawal_amount):
        self.balance -= withdrawal_amount
        self.list.append(f'User withdrew {withdrawal_amount}.')
        return self.balance

    def print_transactions(self):
        print(self.list)

a1 = account()

a1.deposit(500)
a1.deposit(500)
a1.deposit(500)
a1.deposit(500)

a1.withdraw(300)
a1.withdraw(300)
a1.withdraw(300)
a1.withdraw(300)

a1.print_transactions()