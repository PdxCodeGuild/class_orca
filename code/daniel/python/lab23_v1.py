'''
PDX Code Guild
Daniel Eggimann
Lab_23 Version_1
'''

with open('contact_list.csv', 'r') as file:
    lines = file.read().split('\n')
print(lines)

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

def main():
    # generate contact list titles
    keys = key_generator()
    # generate tuples of contact info
    contact_value = value_generator()
    # generate a list of dictionaries, one dictionary for each contact
    contacts = []
    for contact in contact_value:
        contact_dict = contact_tuples(keys, contact)
        contacts.append(contact_dict)
    for i in contacts:
        print(i)        

main()
