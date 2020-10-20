
class ATM:
    def __init__(self, balance = 0.00, amount = 0.00):
        self.balance = balance
        self.amount = amount
        self.transactions = []
        
    def check_balance (self):
        return f"Your balance is ${self.balance}."

    def deposit (self, amount):
        self.amount = amount
        self.balance += self.amount
        self.transactions.append(f"User deposited ${self.amount}")
        return f"Your balance is ${self.balance}."
    
    def check_withdrawal (self, amount):
        self.amount = amount
        if self.balance - self.amount >= 0:
            return True
        else:
            return False
    def withdrawal (self, amount):
        self.amount = amount
        # if self.balance - self.amount >= 0:
        if self.check_withdrawal(amount) == True:
            self.balance -= self.amount
            self.transactions.append(f"User withdrew ${self.amount}")
            return f"Take you your cash. You balancs is ${self.balance}."
        else:
            return f"${self.amount} is too much! You only have ${self.balance} in your account!"
    
    def print_trans(self):
        return (f" Here are the most recent transactions:\n{self.transactions})\n Your balance is: {self.balance})")
    

my_account = ATM()
bank_actions = [ "check balance",  "make withdrawal", "make deposit", "check withdrawal",  "print transactions"]

while True:
    what_to_do = (input("What would you like to do: 'check balance', 'make withdrawal','make deposit', 'check withdrawal', 'print transactions'?\n")).lower()
    if what_to_do in bank_actions:
        if what_to_do == "check balance":
            print(f"Your balance is ${my_account.check_balance()}.")
        elif what_to_do == "make withdrawal":
            amount = float(input ("How much do you want to withdraw?:\n"))
            print(my_account.withdrawal(amount))
        elif what_to_do == "make deposit":
            amount = float(input ("How much do you want to deposit?:\n"))
            print(my_account.deposit(amount))
        elif what_to_do == "check withdrawal":
            amount = float(input ("How much do you want to withdraw?:\n"))
            if my_account.check_withdrawal(amount) == True:
                print("You have enough to do that!")
            else: 
                print("Sorry buddy, you're broke! No can do.")
        elif what_to_do == "print transactions":
            print(my_account.print_trans())
        else:
            print ("Not a possible transaction.")
    try_again = (input("Make another transaction?: 'y' or 'n':\n")).lower()
    if try_again == 'y':
        continue
    else:
        print ("Thanks for banking with Marc.")
        break
