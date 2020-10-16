'''
Lab 23: Contact List
Matthew Chimenti
Version 1 and 2

'''


with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')
    # print(lines)

#grab the data out of the CSV
x = lines[0]
# print(x)

#get the headers
headers = x.split(',')
# print(headers)

#get the data: all the lines below headers
data = lines[1::]
# print(data)
contacts = []
for row in data:
    counter = 0
    contact = {
    }

    # print(row)
    row_split = row.split(',')
    # print(row_split)
    for i in row_split:
        # print(i)
        #keys
        contact[headers[counter]] = i
        counter += 1
    contacts.append(contact)

# print(headers)
# print(contacts)
# print(contact)

def create_contact():
    #get the keys
    # print(headers)

    #get the users info and put the inputs in a list
    list_inputs = [
        input("\tWhat is your name: ").capitalize(),
        input("\tWhat is your costume: ").capitalize(),
        input("\tWhat is your favorite food: ").capitalize(),
        input("\tWhat is your favorite drink: ").capitalize()
    ]

    #put the keys and users info together in a dictionary
    key_user = dict(zip(headers, list_inputs))
    # print(key_user)

    #put the dict in the list of contacts
    contacts.append(key_user)
print(f'Displaying Records: {contacts}')


def retrieve():
    #ask the user for the contacts name
    x = input("Retrieve: Please enter a name of the person who's information you'd like to retrieve? ").capitalize()

    #find the user with the given name
    for name in contacts:
        if name['name'] == x:

            #display their information
            print(f'\t{name}')
            print()
        else:
            pass

def update():
    #ask the user for the contact's name
    x = input("Update: Please enter the users name who's record you'd like to update: ").capitalize()
    print("\tDisplaying record")

    #print that users records
    for name in contacts:
        if name['name'] == x:
            print(f'\t{name}')

            #ask for which attribute they'd like to update
            y = input(f"What record from below would you like to change?\n\t{headers}")

            print(name)

            #ask the user for the value they want to replace it with
            z = input(" What would you like to change the record to? ")
            name[y] = z
            print(f'\t{name}')
            print()

def delete():
    #ask the user for the contact name
    x = input("Delete: Please enter the users name who's record you'd like to delete: ").capitalize()

    for name in range(len(contacts)):
        # print(name)
        # print(x)
        if contacts[name]['name'] == x:



            #remove the contact with the given name from the contact list
            del contacts[name]
            return contacts




create_contact()
retrieve()
update()
print(delete())