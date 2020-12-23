'''
Lab 25: ATM
'''

transactions = []

class Atm:
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        return self.balance

    def deposit(self, deposit):
        self.balance = self.balance + deposit
        return self.balance

    def withdraw(self, withdraw):
        if self.balance - withdraw >= 0:
            self.balance = self.balance - withdraw
            return True
        else:
            print("insufficient funds")
            return False

def print_transactions():
    for trans in transactions:
        if trans > 0:
            print(f"You deposited ${trans}")
        elif trans < 0:
            print(f"You withdrew ${-trans}")


account = Atm()
# print(account.check_balance())



def main():
    selection_input = int(input("""
Hello, welcome to teh Evil Bank Corp ATM. Please selection from the following options:
1: Check your balance
2: Deposit funds
3: Withdraw
4: History
5: Quit
"""))

    if selection_input == 1:
        print(f"You have {account.check_balance()} available.")
        main()
    elif selection_input == 2:
        deposit = int(input("please enter the amount you wish to deposit "))
        account.deposit(deposit)
        transactions.append(deposit)
        main()
    elif selection_input == 3:
        withdraw = int(input("please enter the amount you wish to withdraw "))
        account.withdraw(withdraw)
        transactions.append(-withdraw)
        main()
    elif selection_input == 4:
        print_transactions()
        main()
    elif selection_input == 5:
        print("""
Please remember to grab your card and possessions before leaving this machine.
Have a good day!  @Evil Bank Corp""")
        quit()
main()

