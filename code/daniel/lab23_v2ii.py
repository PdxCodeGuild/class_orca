# GLOBAL VARIABLES
with open('contact_list.csv', 'r') as file:
    lines = file.read().split('\n')

# GLOBAL VARIABLES
# master contact list
mstr_contact = []
# dictionary keys for contact list
keys = lines[0].split(',')

# original values in .csv file
orig_values = []
[orig_values.append(lines[item].split(',')) for item in range(1, len(lines))]
# combining keys with the original contact data provided
for contact in orig_values:
    temp_list = {}
    for i, attribute in enumerate(contact):
        temp_list.update({keys[i]: attribute})
    mstr_contact.append(temp_list)

def input_contact():
    '''Gathers input from the user and adds the information to the master contact list.'''
    contact_name = input("Enter the contact name:  ")
    contact_zodiac = input("Enter the contact zodiac:  ")
    contact_occupation = input("Enter the contact occupation:  ")
    contact_country = input("Enter the contact country:  ")
    user_dict = {keys[0]: contact_name, keys[1]: contact_zodiac, keys[2]: contact_occupation, keys[3]: contact_country}
    print('\nThe following information has been added to the contact list\n')    
    for k, v in user_dict.items():
        print(f"\t",k,v)
    print("\n")
    mstr_contact.append(user_dict)

def look_up_contact():
    '''Gathers user input and prints out the contact info if it exists.'''
    contact_name = input("Enter the contacts name:  ")
    # for-loop to look up contact
    for contact in mstr_contact:
        if contact['name:'] == contact_name:
            print("\n")
            for k, v in contact.items():
                print(f"\t",k,v)
            print("\n")

def update_contact():
    '''Gathers input from user and prints the contact if it extsts.'''
    contact_name = input("Enter the contact name you would like to update:  ")
    attribute = input(f"Enter the contact attribute that you want to update.\nname, zodiac, occupation, country:  ") + ":"
    new_value = input("Enter the new value for that attribute:  ")
    for contact in mstr_contact:
        if contact['name:'] == contact_name:
            contact[attribute] = new_value
            print('\n')
            for k, v in contact.items():
                print(f"\t",k,v)
            print("\n")

def delete_contact():
    contact_name = input("Enter the contact name that you want to delete:  ")
    for i, contact in enumerate(mstr_contact):
        if contact['name:'] == contact_name:
            mstr_contact.pop(i)
            print(f'The contact information for {contact_name} hase been deleted.')

def main():
    while True:
        answer = input('Would you like to add a new contact?\ny/n:  ')  
        if answer not in ['y', 'yes', 'n', 'no']:
            answer = input('Invalid repsonse. Please enter y/n:  ')
        elif answer in ['y', 'yes']:
            input_contact()
        answer = input('Would you like to look up a contact?\ny/n:  ')
        if answer not in ['y', 'yes', 'n', 'no']:
            answer = input('Invalid repsonse. Please enter y/n:  ')
        elif answer in ['y', 'yes']:
            look_up_contact()
        answer = input('Would you like to update an existing contact?\ny/n:  ')
        if answer not in ['y', 'yes', 'n', 'no']:
            answer = input('Invalid repsonse. Please enter y/n:  ')
        elif answer in ['y', 'yes']:
            update_contact()
        answer = input('Would you like to delete an existing contact?\ny/n:  ')
        if answer not in ['y', 'yes', 'n', 'no']:
            answer = input('Invalid repsonse. Please enter y/n:  ')
        elif answer in ['y', 'yes']:
            delete_contact()
        answer = input('Would you like to see the entire contact list?\ny/n:  ')
        if answer not in ['y', 'yes', 'n', 'no']:
            answer = input('Invalid repsonse. Please enter y/n:  ')
        elif answer in ['y', 'yes']:
            print('\n')
            for contact in mstr_contact:
                for k, v in contact.items():
                    print(f'\t',k,v)
                print('\n')
        answer = input('Would you like to review these options again?\ny/n:  ')
        if answer not in ['y', 'yes', 'n', 'no']:
            answer = input('Invalid repsonse. Please enter y/n:  ')
        elif answer not in ['y', 'yes']:
            break

main()