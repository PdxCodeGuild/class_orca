import csv

def update_file(dictionary):
    keys = dictionary[0].keys()
    with open('contacts.csv', 'w', newline='')  as f:
        dict_writer = csv.DictWriter(f, keys)
        dict_writer.writeheader()
        dict_writer.writerows(dictionary)
        return dictionary


def create(dictionary):
    name = input('Contact name?\n> ')
    fav_fruit = input('Contacts favorite fruit?\n> ')
    fav_color = input('Contacts favorite color?\n> ')
    blah = {'name': name, 'favorite fruit': fav_fruit, 'favorite color': fav_color}
    dictionary.append(blah)
    update_file(dictionary)
    return dictionary


def retrieve(dictionary):
    name = input('Enter the name of the contact you want to retrieve\n> ')
    count = 0
    for i in dictionary:
        if name == i['name']:
            count += 1
        else:
            count += 0
        if count > 0:
            print(f'Contact: {i}')
            break
    if count == 0:
        print('''

name not found

        ''')


def update(dictionary):
    name = input('What is the name of the contact you want to change?: ')
    attribute = input('Which attribute are you changing? (name - favorite fruit - favorite color)\n> ')
    changed = input(f'What is the new {attribute}?\n> ')
    for i in dictionary:
        if name == i['name']:
            i[attribute] = changed
            update_file(dictionary)
            return dictionary


def delete(dictionary):
    name = input('What is the name of the contact you want to delete?:   ')
    for i in dictionary:
        if name == i['name']:
            dictionary.remove(i)
            update_file(dictionary)
            return dictionary


def main():
    with open('contacts.csv', 'r') as file:
        lines = file.read().split('\n')
        keys = lines[0].split(',')
        values = lines[1:]


    dictionary = []

    for i in values:
        i = i.split(',')
        dictionary2 = dict(zip(keys, i))
        dictionary.append(dictionary2)

    while True:
        choice = input('''
    Choose one:
    1 - create contact
    2 - retrieve contact
    3 - update contact
    4 - delete contact
    5 - to quit

    > ''').lower()
        if choice == 'create' or choice == 'create a contact' or choice == 'create contact' or choice == '1':
            create(dictionary)
        elif choice == 'retrieve' or choice == 'retrieve a contact' or choice == 'retrieve contact' or choice == '2':
            retrieve(dictionary)
        elif choice == 'update' or choice == 'update a contact' or choice == 'update contact' or choice == '3':
            update(dictionary)
        elif choice == 'delete' or choice == 'delete a contact' or choice == 'delete contact' or choice == '4':
            delete(dictionary)
        elif choice == 'quit' or choice == '5':
            break



main()
