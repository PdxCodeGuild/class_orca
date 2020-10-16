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
    return find_record

#Update record
def update_record():
    find_record = input("Please enter name ")
    for record in contact_obj:
        if record['name'] == find_record:
            #Select which field to change
            #Display input line for that field
            #Re-display entire record
            pass


#CRUD REPL
def edit_db():
    select = input("What would you like to do? Type 'new,' 'view,' 'edit,' 'delete'  or 'done' ")
    if select == "new":
        new_record()
    if select == "view":
        view_record()
edit_db()
    