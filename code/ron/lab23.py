
# *'-.-'*'-.-'*'-.-'*-.-'*-.-'*-.-'*-.-'*'-.-'*'-.-'*'-.-'*
#        Project: Python
# Assignment/Ver: Lab23
#         Author: Ron Mansolilli, ron.mansolilli@gmail.com
#           Date: 10-15-2020
# *'-.-'*'-.-'*'-.-'*-.-'*-.-'*-.-'*-.-'*'-.-'*'-.-'*'-.-'*

#----Instructions and notes-----------------------------------------
''' 

Lab 23: Contact List

'''
#----Modules----------------------------------------------------

import string
import math
import random

#----Global variables, lists, dictionaries----------------------

contacts = []
info = {}
user_data = {}

#----Functions--------------------------------------------------

def main_menu():#------------------------------------------------
    ''' Welcome screen and interface '''

    print('''   
         ***** Welcome! *****

Please select from the following options:

           1. Check/display record
           2. Create record
           3. Delete record
           4. Update record
           5. Save records
           or 'exit'   
''')

    # User menu logic
    choice = ''
    while choice != ('1', '2', '3', '4', 'exit'):
        choice = input('\t>>> ')
        if choice == '1':
            user_info = retrieve_record()
            display_record(user_info)
            choices()                 
        elif choice == '2':
            contacts.append(create_user())
            save_data()
            choices()
        elif choice == '3':
            delete_user() 
            save_data()
            choices()
        elif choice == '4':
            update_user()
            save_data()
            choices()             
        elif choice == '5':
            save_data()
            choices()  
        elif choice == 'exit':
            quit()                  
        else:
            print('\n>>> Invalid selection, try again:\n')
            continue

def user_name_check(user_name):#----------------------------------
    '''Check username'''

    # print(1, user_name)
    # Loop through contact list and look for user
    for user_dict in contacts:
        # print(2, user_dict)
        for key in user_dict:
            # print(3, key)
            if user_dict.get('name') == user_name:
                return user_dict
                break
            
    # If user name not found give option to create account
    print(f' ** {user_name} not found **')                    
    create = input('\nWould you like to create an account (y/n): ')
    if create == "n":
        choices()
    else: 
        contacts.append(create_user(user_name))
        choices()

def choices():#-------------------------------------------
    '''User choice menu'''

    while True:
        yn = input(f'\nWould you like to return to the main menu (y/n): ')
        if yn == 'y':
            main_menu()
        elif yn == 'n':
            print('\n\t** Goodbye **\n')
            exit()
        else:
            print('invalid selection')
            continue

def retrieve_record():#-------------------------------------------
    '''Retrieve record'''

    # Input name and check list
    user_name = input('\nWhat is the name: ')
    user_info = user_name_check(user_name)
    return user_info
    # print(4, user_info) # Code and Error Testing

def display_record(user_info):#-------------------------------------------
    '''Display record''' 

    print(f'''
Record Display
---------------------------

Name: {user_info['name']}
Favorite fruit: {user_info['favorite fruit']}
Favorite color: {user_info['favorite color']}
Favorite animal: {user_info['favorite animal']}''')

def create_user(user_name = ""):#-----------------------------------------
    '''Create user account in dictionary entry'''

    print(f'''
Create Record
---------------------------''')

    # User input and add to contact list
    if user_name == "":
        user_data['name'] = input('\tWhat is your name: ')
    else:
        user_data['name'] = user_name
    user = user_data['name']
    user_data['favorite animal'] = input('What is your favorite animal: ')
    user_data['favorite fruit'] = input('What is your favorite fruit: ')
    user_data['favorite color'] = input('What is your favorite color: ')
    print(f'\nWelcome {user}, you have been successfully added to the borg, ahem, the contact list.  ')
    return user_data

def delete_user():#-----------------------------------------------------
    ''' Delete user dict '''

    print('\nWhat user would you like to delete: \n')
    for user_dict in contacts:
        user = user_dict['name'] 
        print(f'- {user}')
    user_name = input('>>> ')
    for i in range(len(contacts)):
        if contacts[i]['name'] == user_name:
            print(f'\n{user_name} has been eliminated!')
            del contacts[i]
            break

def update_user(user_name = ""):#--------------------------------------
    '''Update user dict'''

    print(f'''
Update Record
---------------------------''')

    # Retrieve user dictionary (data)
    user_info = retrieve_record()    
    # print(0, user_info) # Code and Error Testing
    user_name = user_info['name']
    # print(1, user_name) # Code and Error Testing

    # Input menu
    while True:
        print('\nWhich attribute would you like to change (1, 2, 3, or 4): \n')
        print("1. Favorite animal")
        print("2. Favorite fruit")
        print("3. Favorite color")
        print("4. Finished updating")
        choice = input(">>> ")

        # Menu logic, update data directly to contact list
        if choice not in ("1", "2", "3", "4"):
            print("\nInvalid selection")
            continue
        elif choice == "1":
            for item in contacts:
                if item["name"] == user_name:
                    item["favorite animal"] = input('New favorite animal: ')
        elif choice == "2":
            for item in contacts:
                if item["name"] == user_name:
                    item["favorite fruit"] = input('New favorite fruit: ')
        elif choice == "3":
            for item in contacts:
                if item["name"] == user_name:
                    item["favorite color"] = input('New favorite color: ')
        else:
            break

    print(f'\n{user_name}, you have been successfully updated the record. \n')
 

def save_data():#---------------------------------------------------------
    ''' Save contacts list to the original CSV '''

    with open('contacts.csv', 'w') as contact_file:

        # Pull keys and write to .csv
        keys = contacts[0].keys()
        keys = ','.join(keys)
        # keys = f'{keys}'
        contact_file.write(keys)

        # Pull values and write to .csv
        for i in contacts:
            temp = i['name'], i['favorite color'], i['favorite animal'], i['favorite fruit']
            temp = ','.join(temp)
            line = f'\n{temp}'
            contact_file.write(line)

#--------Main Code---------------------------------------------

def main(): 

    # Open .csv file
    with open('contacts.csv', 'r') as file:
        lines = file.read().split('\n')

    # Breakout keys into unique list and delete from .csv
    keys = lines[0].split(',')
    del lines[0]

    # Populate contact list with user dicts
    for x in range(len(lines)):
        info = {}
        # Build temp list to hold user data
        temp = lines[x].split(',')
        # Take temp data and build dict
        for y in range(len(temp)):
            info[keys[y]] = temp[y]
        # Drop user dict into contacts list
        contacts.append(info)

    # Main menu
    main_menu()
    
main()

