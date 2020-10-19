class account:

    def __init__(self):
        self.balance = 0

    def check_balance(self):
        return self.balance
    
    def deposit(self, deposit_amount):
        self.balance += deposit_amount
        return self.balance

    def check_withdrawal(self, check_withdrawal_amount):
        if check_withdrawal_amount > self.balance:
            return False
        else:
            return True
    
    def withdraw(self, withdrawal_amount):
        self.balance -= withdrawal_amount
        return self.balance