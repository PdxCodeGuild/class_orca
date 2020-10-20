class ATM:
    def __init__(self):
        self.bal = 50
        self.check = False
    def check_balance(self):
        return self.bal

    def deposit(self,amount):
        self.bal = self.bal + amount
        return self.bal

    def withdraw(self,amount):
        if self.check == True:
            self.bal = self.bal - amount
            return self.bal
        else:
            pass

    def check_withdraw(self,amount):
        if self.bal < amount:
            print("I'm sorry, Dave. I'm afraid I can't do that.\n")
            self.check = False
            return self.check
        else:
            print('kk')
            self.check = True
            return self.check
def again():
    choices = input('you done? \n1. yea \n2. nah  ')
    if choices == 1:
        choices = 4
        return choices
    elif choices == 2:
        choices = 5
        
bank1 = ATM()
balance = bank1.check_balance()
while True:
    choices = input('ay. u wanna: \n1. check balance \n2. deposit \n3. withdraw \n4. dip\n')
    try:
        choices = int(choices)
    except ValueError:
        print('nah, try again\n')
        choices = 0

    if choices == 1:
        print(f'aight, u got {balance} in the bank rn. \n')
        # again()

    elif choices == 2:
        amt = float(input('k, how much  '))
        bank1.deposit(amt)
        balance = bank1.check_balance()
        print(f'cool, u got {balance} in the bank now.\n')

    elif choices == 3:
        amt = float(input('k, how much u finna take?  '))
        bank1.check_withdraw(amt)
        bank1.withdraw(amt)
    
    elif choices == 4:
        break
    
    balance = bank1.check_balance()

print('cool.  peace.')