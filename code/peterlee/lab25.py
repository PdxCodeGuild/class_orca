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

def main():
    a1 = account()
    while True:
        option = input('What would you like to do (deposit, withdraw, check balance, history, done)? ')
        if option == 'done':
            break
        elif option == 'deposit':
            ask_deposit = float(input('How much would you like to deposit? '))
            a1.deposit(ask_deposit)
        elif option == 'withdraw':
            ask_withdraw = float(input('How much would you like to withdraw? '))
            a1.withdraw(ask_withdraw)
        elif option == 'check balance':
            balance = a1.check_balance()
            print(f'Your balance is {balance}.')
        elif option == 'history':
            print(f'Your transaction history is:')
            a1.print_transactions()

main()


