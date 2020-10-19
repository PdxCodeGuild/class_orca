##############################################################################
# John Fial, PDX Code Guild, 2020-2021
# https://github.com/PdxCodeGuild/class_orca/blob/main/1%20Python/labs/lab25-ATM.md

# Step 8 v2 make an account history function... Make the deposit/withdraw functions
# add a string to a list of 'User {Action} {amount} 
# 8c then add new function print_transactions() to display the account history
##############################################################################
# ***************************** WORKING FROM HERE *****************************
# ***************************** ^^^^^^^^^ TO HERE *****************************


class ATM(): 

    def __init__(self, balance=0):        
        self.balance = balance
        self.history = []
        self.datetime = 'Today'
        self.history.append(f'Date: {self.datetime}. Account opened with starting balance of ${self.balance}.')

    def check_balance(self): # shouldn't balance be started in the init function?
        print(f'Balance is ${self.balance}.')
        return self.balance
        
    def deposit(self,amount):
        # TODO REJECT STRING INPUT
        # TODO REJECT STRING INPUT
        # TODO REJECT STRING INPUT
        if amount <= 0:
            print(f'Invalid entry. Please use the withdrawl function to make a withdrawl. Balance is ${self.balance}.')
            return self.balance
        elif amount >0:
            self.balance += amount
            print(f'${amount} deposited. You new balance is ${self.balance}.')
            self.history.append(f'Date: {self.datetime}. Deposit: ${amount}. Balance is ${self.balance}.')
        else:
            print(f'Invalid input. Balance is ${self.balance}.')
        return self.balance

    def print_transactions(self):
        print('Beginning transaction history...')
        print(self.history)
        print('...end of transaction history.')
    
    def check_withdrawl(self, amount):
        if self.balance > amount and amount > 0:
            return True
        else:
            return False
        print('invalid!')

    def withdraw(self,amount):

        self.check_withdrawl(amount)

        if self.check_withdrawl(amount) == True:
            self.balance -= amount
            print(f'${amount} withdrawn. You new balance is ${self.balance}.')
            self.history.append(f'Date: {self.datetime}. Withdrawl: ${amount}. Balance is ${self.balance}.')
            return self.balance
        else:
            self.history.append(f'Date: {self.datetime}. REJECTED Withdrawl for amount: ${amount}. Balance is ${self.balance}.')
            print(f'Sorry! Current balance is ${self.balance}; but you tried to withdraw ${amount}.')
            return self.balance



account1 = ATM(505)

account1.deposit(2)
account1.deposit(-100)
account1.deposit(2)
# account1.print_transactions()
# print(account1.check_withdrawl(-555))
account1.withdraw(-55)



# add call function for REPL under each if statement... # should NOT have to do this if you call it one time before!
# NOTE FIX # TypeError: '>' not supported between instances of 'int' and 'str'
# NOTE FIX # TypeError: '>' not supported between instances of 'int' and 'str'
# NOTE FIX # TypeError: '>' not supported between instances of 'int' and 'str'
# print(account1.balance) # NOTE this is where __str__ comes in useful or necessary

































##############################################################################
# Step 10 Creae the REPL Loop, start with the CRUD thing from contacts list and change wording
def next_operation():

    user_input = input(f'Enter next operation: ')    # user_input = 'create' # TEMP INPUT ### REMEMBER that invalid input here WILL LOOP, which is correct functionality!
    return user_input


def main(account):
    print('Welcome to ATM v1!')
    print(f'Acceptable operations are, without quotes: \"check balance\", \"deposit\", \"withdraw\", \"history\", or \"exit\": ')
    # TODO STRIP EXTRA CHARACTERS, LOWERCASE, ETC...

    user_input = next_operation()

    while user_input != 'exit':
        if user_input == 'check balance':  
            check_balance() # NOTE balance?
            ########### NOTE 
            user_input = next_operation()

        elif user_input == 'deposit':
            print('Please type #################: ') 
            user_input = next_operation()

        elif user_input == 'withdraw':
            ########### NOTE 
            print('Please type #################: ')   
            user_input = next_operation()

        elif user_input == 'history':
            print('Account History: ')
            user_input = next_operation()

        else:            
            print('Invalid input!')
            user_input = next_operation()
            pass

    else: # if user_input is 'exit'...
        return 

################# call it!
# main()
################### FINAL WORK: FIX ENTERING NAME IN DELETE...
################### FINAL WORK: FIX ENTERING COMMAS AND OTHER DANGEROUS CHARACTERS!





print('     ~~~  PROGRAM ENDED  ~~~       ')
##############################################################################
# https://github.com/PdxCodeGuild/class_orca/blob/main/1%20Python/labs/lab25-ATM.md