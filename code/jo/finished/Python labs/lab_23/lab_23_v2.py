with open ('contacts.csv', 'r') as file:
    lines = file.read().split("\n")

        



contacts_tup_list = []
contacts_list = []
contacts = [i.split(',') for i in lines]

key = contacts.pop(0)

for i in contacts:
    entry = list(zip(key,i))
    contacts_tup_list.append(entry)

for i in contacts_tup_list:
    contacts_list.append(dict(i))

contacts_list = [dict(i) for i in contacts_tup_list]


def create(contact,key):
    new_contact = {}
    for i in key:
        new_contact[i] = input(f"What is the new agent's {i}? ")
    contacts_list.append(new_contact)
    





while True:
    crud = input('Would you like to [c]reate, [r]eview, [u]pdate, [d]elete, or [q]uit? ')
    if crud == 'c':
        create(contacts_list,key)
    elif crud == 'r':
        c_record = input("Which record would you like to view? ")
        for contact in contacts_list:
            if c_record == contact["name"]:
                print(contact)
    elif crud == 'u':
        name = input("Whose record would you like to update? ")
        change = input("What would you like to update? (name,ship,handle,spcialty) ")
        update = input(f"What would you like to change agent's {change} to? ")
        for i in contacts_list:
            if i["name"] == name:
                i[f'{change}'] = update 
                print(f"The new record is: {i}")
    elif crud == 'd':
        d_record = input(f"Whic record would you like to delete?")
        for i in contacts_list:
            if i["name"] == d_record:
                contacts_list.remove(i)
                print(f"The record for {d_record} has been deleted.")
                print(contacts_list)
    elif crud == 'q':
        break
    else:
        print("please try again")
    

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




with open('contacts.csv', 'w') as file:
    file.write(str(new_csv))