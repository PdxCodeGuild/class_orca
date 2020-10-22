class ATM:
    def __init__(self):
        self.bal = 50
        self.check = False
        self.transactions = []
    def check_balance(self):
        return self.bal

    def deposit(self,amount):
        self.bal = self.bal + amount
        self.transactions.append(f" desposited ${amount}") 
        return self.bal

    def withdraw(self,amount):
        if self.check == True:
            self.bal = self.bal - amount
            self.transactions.append(f" withdrew ${amount}")
            return self.bal
        else:
            pass

    def check_withdraw(self,amount):
        if self.bal < amount:
            print("\nI'm sorry, Dave. I'm afraid I can't do that.\n")
            self.check = False
            return self.check
        else:
            print("\nkk, money's in ur pocket\n")
            self.check = True
            return self.check
    def print_transactions(self):
        print(f"\nhere's what u did this time: u{(', then'.join(self.transactions))}\n")
        
bank1 = ATM()
balance = f'${bank1.check_balance()}'
while True:
    choices = input('ay. u wanna: \n1. check balance \n2. deposit \n3. withdraw \n4. transaction history\n5. dip\n')
    try:
        choices = int(choices)
    except ValueError:
        print('nah, try again\n')
        choices = 0

    if choices == 1:
        if balance == 0:
            print('\nu got NOTHIN in the bank. \n')
        else:
            print(f'\naight, u got ${balance} in the bank rn. \n')

    elif choices == 2:
        amt = float(input('\nk, how much  ').strip('$'))
        bank1.deposit(amt)
        balance = bank1.check_balance()
        print(f'cool, u got ${balance} in the bank now.\n')

    elif choices == 3:
        amt = float(input('\nk, how much u finna take?  ').strip('$'))
        bank1.check_withdraw(amt)
        bank1.withdraw(amt)
    
    elif choices == 4:
        bank1.print_transactions()

    elif choices == 5:
        break
    
    balance = bank1.check_balance()

print('\ncool.  peace.')