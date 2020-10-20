""" 
Still to do:

add view all
fix c
functions
 """


# opens csv and splits each line into a list element
with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')

contacts = []
contacts_tup_list = []
contacts_list = []

def make_contacts():
    # makes each element of lines list into its own list
    for i in lines:
        contacts.append(i.split(","))

    # makes first line of csv it's own list then removes from contacts list. will be used as key in final dicts
    key1 = contacts.pop()

    # makes each contact a list of key/value tuples
    for i in contacts:
        entry = list(zip(key1,i))
        contacts_tup_list.append(entry)

    # turns list of tuples to list of dicts
    for i in contacts_tup_list:
        contacts_list.append(dict(i))
    return contacts_list



def add_contact(new_contact):
        # makes each element of lines list into its own list
    for i in lines:
        contacts.append(i.split(","))

    # makes first line of csv it's own list then removes from contacts list. will be used as key in final dicts
    key1 = contacts.pop()
    contacts.append(new_contact)
    # makes each contact a list of key/value tuples
    for i in contacts:
        entry = list(zip(key1,i))
        contacts_tup_list.append(entry)

    # turns list of tuples to list of dicts
    for i in contacts_tup_list:
        contacts_list.append(dict(i))
    return contacts_list


contacts_list = make_contacts()

crud = input("\nWhat would you like to do?\nCreate a new record? enter 'c' \nRetrieve a record? enter 'r' \nUpdate a record? enter 'u' \nDelete a record? enter 'd' \nexit? enter 'e' \n")
while True:
    if crud == 'c':
        name = input("What is the agent's name? ")
        town = input("What is the agent's ship? ")
        handle = input("What is the agent's handle? ")
        specialty = input("What is the agent's specialty? ")
        new_contact = [name,town,handle,specialty]
        # contacts.append(new_contact)
        contacts_list = add_contact(new_contact)
        print(contacts_list)
        crud = input("\nWhat would you like to do?\nCreate a new record? enter 'c' \nRetrieve a record? enter 'r' \nUpdate a record? enter 'u' \nDelete a record? enter 'd' \nexit? enter 'e' \n")
    elif crud == 'r':
        agent = input("Whose record would you like to view? ")
        request = []
        for i in contacts_list:
            if i["name"] == agent:
                request.append(i)
        if request:
            print(request)
        else:
            print('There were no records with that name')
        crud = input("\nWhat would you like to do?\nCreate a new record? enter 'c' \nRetrieve a record? enter 'r' \nUpdate a record? enter 'u' \nDelete a record? enter 'd' \nexit? enter 'e' \n")
        
    elif crud == 'u':
        name = input("Whose record would you like to update? ")
        change = input("What would you like to update? (name,hometown,handle,spcialty) ")
        update = input(f"What would you like to change agent's {change} to? ")
        for i in contacts_list:
            if i["name"] == name:
                i[f'{change}'] = update 
                print(f"The new record is: {i}")
        crud = input("\nWhat would you like to do?\nCreate a new record? enter 'c' \nRetrieve a record? enter 'r' \nUpdate a record? enter 'u' \nDelete a record? enter 'd' \nexit? enter 'e' \n")

    elif crud == 'd':
        record = input("What is the name on the record you would like to delete? ")
        
        for i in contacts_list:
            if i["name"] == record:
                contacts_list.remove(i)
                print(f"The record for {record} has been deleted.")
                print(contacts_list)
                crud = input("\nWhat would you like to do?\nCreate a new record? enter 'c' \nRetrieve a record? enter 'r' \nUpdate a record? enter 'u' \nDelete a record? enter 'd' \nexit? enter 'e' \n")
    elif crud == "e":
        break
    else:
        print("\nThat is an invalid entry. Please try again.\n")
        crud = input("\nWhat would you like to do?\nCreate a new record? enter 'c' \nRetrieve a record? enter 'r' \nUpdate a record? enter 'u' \nDelete a record? enter 'd' \nexit? enter 'e' \n")


# # print(lines)
# # print(key1)
# # print(contacts)
# # print(contacts_tup_list)
# print(contacts_list)


#--------------------------------------------------------
# reverses the csv to list of dictionaries process to write to contacts.csv

# turns list of dictionaries to list of tuples
contacts = []
for d in contacts_list:
    contact = [(k,v) for k,v in d.items()]
    contacts.append(contact)

# unzips the tuples into lists
uz_contacts = []
for i in contacts:
    uz_contact = list(zip(*i))
    uz_contacts.append(uz_contact)

# separates the key element and contacts within each contact list and recombines into one list
new_csv = []
for l in uz_contacts:
    for i in l:
        key = l[0]
        contact = l[1]
    new_csv.append(contact)
new_csv.insert(0,key)

# turns the list into a string and formats back to original contacts.csv format.
new_csv = [','.join(i) for i in new_csv]
new_csv = str(new_csv).strip('[]')
new_csv = new_csv.replace(" ",'')
new_csv = new_csv.replace("','",'\n')
new_csv = new_csv.strip("'")




with open('contacts_out.csv', 'w') as file:
    file.write(str(new_csv))





