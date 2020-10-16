#Lab23 - Contact List

#Convert csv file to list of dictionaries
with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')
    print(lines)

contact_obj = []

key_list = lines[0].split(',')
print(key_list)

for i in range (1, len(lines), 1):
    lines[i] = lines[i].split(',')
print(lines, "lines list of lists")

for i in range(1, len(lines)):
    entry = dict(zip(key_list, lines[i]))
    contact_obj.append(entry)
print(contact_obj, "contact dictionary")

#Create new record
def new_record():
    add_name = input("Name? ")
    add_fav_animal = input("Favorite animal?  ")
    add_fav_band = input("Favorite band?  ")
    add_fav_tea = input("Favorite kind of tea? ")

    contact_obj.append({'name': add_name, 'fav_animal': add_fav_animal, 'fav_band': add_fav_band, 'fav_tea': add_fav_tea})

    print(f'New record: {add_name, add_fav_animal, add_fav_band, add_fav_tea}')
    print(contact_obj)

    edit_db()

    return add_name, add_fav_animal, add_fav_band, add_fav_tea

#Read record
def view_record():
    find_record = input("Please enter name ")
    for record in contact_obj:
        if record['name'] == find_record:
            print(record)
    
    edit_db()
    return record

#Update record
def update_record(): 
    find_record = input("Please enter name ")
    for record in contact_obj:
        if record['name'] == find_record:
            select_change = input("What value would you like to change? Choose name, animal, band or tea  ")
            if select_change == 'name':
                new_name = input("Name? ")
                record['name'] = new_name
            if select_change == 'animal':
                new_animal = input("Favorite animal? ")
                record['fav_animal'] = new_animal
            if select_change == 'band':
                new_band = input('Favorite band? ')
                record['fav_band'] = new_band
            if select_change == 'tea':
                new_tea = input("Favorite kind of tea? ")
                record['fav_tea'] = new_tea      
        print("Updated record: ", record)
    
    edit_db()
    return record

#Delete record
def delete_record():
    find_record = input("Please enter name ")
    for i in range(len(contact_obj)):
        if contact_obj[i]['name'] == find_record:
            del contact_obj[i]
            break
    print(f'New contact list: {contact_obj}')
    
    edit_db()
    return contact_obj

#Convert dictionary to strings
def back_to_strings():
    # separator = ', '
    # key_string = separator.join(key_list)
    print(key_list)
    print(lines)

#CRUD REPL
def edit_db():
    select = input("What would you like to do? Type 'new,' 'view,' 'edit,' 'delete'  or 'done' ")
    if select == "new":
        new_record()
    if select == "view":
        view_record()
    if select == "edit":
        update_record()
    if select == "delete":
        delete_record()
    if select == "done":
        back_to_strings()
        # write_file()

edit_db()



# #Write new contact list to CSV
# def write_file():
#     with open('contacts.csv', 'w') as file:
#         file.write(contact_obj)
#     print(contact_obj)
#     exit()
    