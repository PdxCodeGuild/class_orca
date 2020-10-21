class ATM:
    def __init__(self):
        self.__balance = 0
        self.__list = []

    def check_balance(self):
        return self.__balance
    
    def deposit(self, deposit_amount):
        self.__balance += deposit_amount
        self.__list.append(f'User deposited ${deposit_amount}.')
        return self.__balance

    def check_withdrawal(self, check_withdrawal_amount):
        return self.__balance > check_withdrawal_amount
          
    def withdraw(self, withdrawal_amount):
        if self.check_withdrawal(withdrawal_amount) == True:
            self.__balance -= withdrawal_amount
            self.__list.append(f'User withdrew ${withdrawal_amount}.')
        else:
            raise ValueError("Your balance is too low.")

    def print_transactions(self):
        print("\n".join(self.__list))


def main():
    a1 = ATM()
    while True:
        option = input('What would you like to do (deposit, withdraw, check balance, history, done)? ')
        if option == 'done':
            break
        elif option == 'deposit':
            ask_deposit = float(input('How much would you like to deposit? '))
            a1.deposit(ask_deposit)
        elif option == 'withdraw':
            ask_withdraw = float(input('How much would you like to withdraw? '))
            try:
                a1.withdraw(ask_withdraw)
            except ValueError as e:
                print(e)
        elif option == 'check balance':
            balance = a1.check_balance()
            print(f'Your balance is ${balance}.')
        elif option == 'history':
            print(f'Your transaction history is:')
            a1.print_transactions()

main()


