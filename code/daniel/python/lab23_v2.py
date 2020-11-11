'''
PDX Code Guild
Daniel Eggimann
Lab_23 Version_2
'''

# GLOBAL VARIABLES
with open('contact_list.csv', 'r') as file:
    lines = file.read().split('\n')

# Master Contact List
contacts = []

def key_generator():
    '''Converts .cvs header to a list of keywords for dictionary use'''
    # keywords for dictionary 
    keys = str(lines[0]).replace(',', ', ')
    keys = keys.split(', ')
    # print(keys)
    return keys

def value_generator():
    '''Converts .cvs text to a list of lists per contact '''
    dict_values = []
    for item in range(1, len(lines)):
        values = str(lines[item].replace(',', ', '))
        values = values.split(', ')
        dict_values.append(values)
    # print(dict_values)
    return dict_values

def contact_tuples(keys, contact):
    '''Combines the key and value inputs to generate a list of dictionaries for every cantact input'''
    contact_dict = {}
    for item in range(len(contact)):
        contact_dict.update({keys[item]: contact[item]})
    # print(contact_dict)
    return contact_dict

def contact_input():
    contact_name = input("Enter the contact name:  ")
    contact_zodiac = input("Enter the contact zodiac:  ")
    contact_occupation = input("Enter the contact occupation:  ")
    contact_country = input("Enter the contact country:  ")
    user_list = contact_name+','+contact_zodiac+','+contact_occupation+','+contact_country
    return user_list

def contact_look_up():
    '''Gathers user input and returns matching dictionary k,v combo if it exists.'''
    contact_name = input("Enter the contacts name:  ")
    contact_info = ''
    i = 0
    for name in contacts:
        if contact_name == contacts[i]['name:']:
            for k, v in contacts[i].items():
                contact_info += k + ' ' + v + "\n"
            break
        else:
            i += 1
    return contact_info

def update_contacts():
    contact_to_update = input("Enter the contact name you would like to update:  ")
    attribute = input(f"Enter the contact attribute that you want to update.\nname, zodiac, occupation, country:  ") + ":"
    new_value = input("Enter the new value for that attribute:  ")
    i = 0
    for name in contacts:
        if contact_to_update == contacts[i]['name:']:
            contacts[i][attribute] = new_value
            break
        else:
            i += 1

def delete_contact():
    delete_contact = input("Enter the contact name that you want to delete:  ")
    i = 0
    for name in contacts:
        if delete_contact == contacts[i]['name:']:
            contacts.pop(i)
            break
        else:
            i += 1

def main():
    # generate contact list titles
    keys = key_generator()
    answer = input("Would you like to add a new contact?\ny/n:  ")
    if answer == 'y':
        lines.append(contact_input())
    # generate tuples of contact info
    contact_value = value_generator()
    # generate a list of dictionaries, one dictionary for each contact
    for contact in contact_value:
        contacts.append(contact_tuples(keys, contact)) 
    # look up contact
    answer = input("Would you like to look up a contact?\ny/n:  ")
    if answer == 'y':
        contact_info = contact_look_up()
        print(contact_info)
    answer = input("Would you like to update an existing contact?\ny/n:  ")
    if answer == 'y':
        update_contacts()
    answer = input("Would you like to delete an existing contact?\ny/n:  ")
    if answer == 'y':
        delete_contact()
    
main()
i = 0
for contact in contacts:
    for k, v in contacts[i].items():
        print(f"\t",k,v)
    print("\n")
    i += 1


    
    

