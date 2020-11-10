accounts = 0

class ATM:
    def __init__(self):
        '''Stores the balance of the account'''
        self.balance = 0
        self.transactions = []
    
    def check_balance(self):
        '''Returns the available balance of the account'''
        self.transactions.append(f'User checked available balance. Available balance: ${self.balance:,.2f}')
        return self.balance

    def deposit(self, amount):
        '''Adds the deposited amount to the account.'''
        self.balance += amount
        self.transactions.append(f'User deposited ${amount:,.2f} into the account. Available balance: ${self.balance:,.2f}') 

    def check_withdrawal(self, amount):
        '''Verifies whether or not the requested funds are availble 
        in the account and returns a True value if they are'''
        if self.balance < amount:
            self.transactions.append(f'User attempted to withdraw insufficient funds of ${amount:,.2f}') 
            print(f'Insufficient funds. Please enter a different amount. Available funds ${self.balance:,.2f}')
        return self.balance >= amount

    def withdraw(self, amount):
        '''Subtracts the requested funds from the avaiable balance of the account.'''
        self.balance -= amount
        self.transactions.append(f'User withdrew ${amount:,.2f} from the account. Available balance: ${self.balance:,.2f}.')

user = ATM()
while True:
    
    # menu
    answer = int(input(f'''
    Which operation would you like to perform:
    Enter (1) to check your balance
    Enter (2) to make a deposit
    Enter (3) to make a withdrawal
    Enter (0) to quit

    \t> '''))
    
    # check balance
    if answer == 1:
        balance = user.check_balance()
        print(f"\n\tYour available balance is: ${balance:,.2f}")
    
    # make deposit
    elif answer == 2:
        amount = int(input('\n\tHow much would you like to deposit?\n\t> '))
        user.deposit(amount)
        # print(f"\n\tYour available balance is: ${user.balance}")

    # make withdrawal
    elif answer == 3:
        while True:
            amount = int(input('\n\tHow much would you like to withdrawal?\n\t> '))
            while user.check_withdrawal(amount) == False:
                amount = int(input('\n\tHow much would you like to withdrawal?\n\t> '))
                continue
            while user.check_withdrawal(amount):
                user.withdraw(amount)
                # print(f"\n\tYour available balance is: ${user.balance}")
                break
            break

    # exit menu
    elif answer == 0:
        print('User Transaction Log')
        for item in user.transactions:
            print(f'>{item}')
        break
