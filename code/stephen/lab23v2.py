with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')
    # print(lines)

contacts = []

for line in range(len(lines)):
    keys = lines[0]
    vals = lines[line]
    keys = keys.split(',')
    vals = vals.split(',')
    kvdict = dict(zip(keys, vals))
    contacts.append(kvdict)

# create a record
def create_contact():
    while True:    
        create_input = input('Please enter the contacts name:\n>'), input('Enter in their favorite color:\n>'),input('Enter in their favorite number:\n>'), input('Enter in their favorite food:\n>')
        create_new = dict(zip(keys, create_input))
        create_check = input(f'You have entered {create_input}.  Is this correct?\ny/n:')
        if create_check == 'y':
            contacts.append(create_new)
            print('Contact added!')
            main_menu()
        elif create_check == 'n':
            print('Try again!')
            create_input = input('Please enter the contacts name:\n>'), input('Enter in their favorite color:\n>'),input('Enter in their favorite number:\n>'), input('Enter in their favorite food:\n>')
            create_new = dict(zip(keys, create_input))
            create_check = input(f'You have entered {create_input}.  Is this correct?\ny/n:')
        main_menu()
    
def retrieve_contact():
    get_contact = input('Enter the name of the contact you would like to retireve:\n>')
    for x in contacts:
        if get_contact == x['name']:
            print(x)
    main_menu()

def retrieve_plus():
    con = input('Enter the name of the contact you would like to retireve:\n>')
    for record in contacts:
        if record['name'] == con:
            return record


def update_contact():
    print('The contacts that are available to update are:')
    for x in contacts:
        print(x['name'])
    record = retrieve_plus()
    update_cat = int(input('''Which category would you like to update?
    1) Update contact name
    2) Update favorite color
    3) Update favorite number
    4) Update favorite food
    5) Return to Main Menu
    >'''))
    if update_cat == 1:
        record['name'] = input('What would you like to change the name to?\n>')
        print(f'The contact has been updated to {record}!')
        main_menu()
    if update_cat == 2:
        record['favorite color'] = input('What would you like to change the favorite color to?\n>')
        print(f'The contact has been updated to {record}!')
        main_menu()
    if update_cat == 3:
        record['favorite number'] = input('What would you like to change the favorite number to?\n>')
        print(f'The contact has been updated to {record}!')
        main_menu()
    if update_cat == 4:
        record['favorite food'] = input('What would you like the change the favorite food to?\n>')
        print(f'The contact has been updated to {record}!')
        main_menu()
    if update_cat == 5:
        main_menu()

def del_contact():
    print('The contacts that are available to delete are:')
    for x in contacts:
        print(x['name'])
    record = retrieve_plus()
    usure = input('Press y to delete this contact and n to return to the main menu.\n>')
    if usure == 'y':
        contacts.remove(record)
        print('Contact has been deleted.')
        main_menu()
    elif usure == 'n':
        main_menu()

def main_menu():
    main_menu = input('Would you like to go back to the main menu?  Enter y for yes and n for quit:\n>')
    if main_menu == 'y':
        main()
    elif main_menu == 'n':
        quit()

def file_write:
    k = ','.join(keys)

def main():
    user_input = int(input('''Welcome to the Contact List!
    Please select an option from the following menu:

    1) Create a new contact
    2) View a contact in the list
    3) Update an exsisting contact
    4) Delete a contact
    5) Quit program
    >''' ))
    if user_input == 1:
        create_contact()
    elif user_input == 2:
        retrieve_contact()
    elif user_input == 3:
        update_contact()
    elif user_input == 4:
        del_contact()
    elif user_input == 5:
        quit()
    else:
        print('Invalid selection!  Try again.')
        user_input = int(input('''Welcome to the Contact List!
    Please select an option from the following menu:

    1) Create a new contact
    2) View contacts in list
    3) Update an exsisting contact
    4) Delete a contact
    5) Quit program
    >''' ))

main()

# retrieve a record

# update a record

# delete a record

# print(contacts)