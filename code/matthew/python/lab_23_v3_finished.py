'''
Lab 23: Contact List
Matthew Chimenti
Version 3

'''

save_list = []

with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')
    # print(lines)

#grab the data out of the CSV (headers)
line = lines[0]
# print(line)

#get the headers
headers = line.split(',')
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

def main_menu():
    main_menu = input('Would you like to go back to the menu?  Enter "y" for yes or "n" to quit: ')
    if main_menu == 'y':
        main()
    elif main_menu == 'n':
        quit()

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
    # print(f'Displaying Records: {contacts}')
    print()

    saving(contacts)
    main_menu()

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

        saving(contacts)
        print()
        main_menu()

def update():
    #ask the user for the contact's name
    x = input("Update: Please enter the users name who's record you'd like to update: ").capitalize()
    print("\tDisplaying record")

    #print that users records
    for name in contacts:
        if name['name'] == x:
            print(f'\t{name}')
            print()

            #ask for which attribute they'd like to update
            y = input(f'''What record from below would you like to change?\n\t{headers}
    ''')


            print(name)

            #ask the user for the value they want to replace it with
            z = input('''What would you like to change the record to? 
    ''')
            name[y] = z
            # print(f'\t{name}')

            saving(contacts)
            print()
            main_menu()

def delete():
    #ask the user for the contact name
    x = input("Delete: Please enter the users name who's record you'd like to delete: ").capitalize()

    for name in range(len(contacts)):
        # print(name)
        # print(x)
        # print(contacts[name]["name"],x )
        if contacts[name]['name'] == x:

            #remove the contact with the given name from the contact list
            del contacts[name]
            # print(contacts)
            saving(contacts)

            main_menu()
            # return contacts



def saving(contacts):
    # print(headers)
    csv_contacts = ",".join(headers)
    first_contact = contacts[0]
    # print(contacts)
    row = []
    # print(csv_contacts)
    row.append(csv_contacts)
    for people in range(len(contacts)):
        # print(contacts[people].values())
        each_peoples_list = list(contacts[people].values())
        # print(each_peoples_list)
        each_peoples_string = ",".join(each_peoples_list)
        # print(each_peoples_string)
        row.append(each_peoples_string)
        # print(row)

    with open('contacts.csv', 'w') as file:
        file.write('\n'.join(row))

    main_menu()

def main():
    selection_input = int(input("""
Please select an option from the menu: 
1: Create an new contact
2: View an existing contact
3: Update an existing contact
4: Delete a contact
5: Quit program
"""))

    if selection_input == 1:
        create_contact()
    elif selection_input == 2:
        retrieve()
    elif selection_input == 3:
        update()
    elif selection_input == 4:
        delete()
    elif selection_input == 5:
        quit()
main()


