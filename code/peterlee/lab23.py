#function to create a dictionary using keys from the first line of the csv file and values from each line after the 
#keys line in the csv file
def update_contacts_list():
    file = open('contacts.csv', 'r')
    contents = file.read()
    lines = contents.split('\n')
    keys = lines[0].split(',')
    lines_list = [lines[x].split(',') for x in range(1, len(lines))]
    contacts_list = []
    for a in range(0, len(lines_list)):
        z = lines_list[a]
        new_dict = {}
        new_dict[keys[0]] = z[0]
        new_dict[keys[1]] = z[1]
        new_dict[keys[2]] = z[2]
        new_dict[keys[3]] = z[3]
        contacts_list.append(new_dict)
    file.close()
    return contacts_list

#function to append a new row into the csv file
def create_crud(b, c, d, e):
    file_create = open('contacts.csv', 'a')
    file_create.write('\n')
    file_create.write(f'{b},{c},{d},{e}')
    file_create.close()
    return

#function to retrieve information using a name from the csv file
def retrieve_crud(f, g):
    return [elem for elem in g if elem['name'] == f]

#function to update an attribute of an entry in the csv file
def update_crud(h, i, j, k):
    temp_list = [elem for elem in k if elem['name'] == h]
    previous_attribute = temp_list[0][i]
    file_update = open('contacts.csv')
    file_update = ''.join([t for t in file_update])
    file_update = file_update.replace(previous_attribute, j)
    new_file = open('contacts.csv','w')
    new_file.writelines(file_update)
    new_file.close()
    return

#function to delete a line in the csv file based on the contact name
def delete_crud(l, m):
    temp_list_two = [elem for elem in m if elem['name'] == l]
    temp_name = temp_list_two[0]['name']
    temp_favoritefruit = temp_list_two[0]['favorite fruit']
    temp_favoritecolor = temp_list_two[0]['favorite color']
    temp_city = temp_list_two[0]['city']
    delete_line = f'{temp_name},{temp_favoritefruit},{temp_favoritecolor},{temp_city}'
    file_update_two = open('contacts.csv')
    file_update_two = ''.join([t for t in file_update_two])
    file_update_two = file_update_two.replace(delete_line, '')
    file_update_two = file_update_two.replace('\n\n', '\n')
    new_file_two = open('contacts.csv','w')
    new_file_two.writelines(file_update_two)
    return


    

def main():
    updated_contacts_list = update_contacts_list()

    #REPL loop for CRUD
    which_crud = input("Select a choice by typing it (create, retrieve, update, delete or done): ")
    while True:
        #prints final list when user is finished
        if which_crud == 'done':
            break
        elif which_crud == 'create':
            new_name = input('Enter a new name: ')
            new_favorite_fruit = input('Enter their favorite fruit: ')
            new_favorite_color = input('Enter their favorite color: ')
            new_city = input('Enter their current city: ')
            create_crud(new_name, new_favorite_fruit, new_favorite_color, new_city)
            update_contacts_list()
            which_crud = input("Select another choice by typing it (create, retrieve, update, delete or done): ")
        elif which_crud == 'retrieve':
            retrieve_name = input('Enter the name whose information you want to retrieve: ')
            retrieve_info = retrieve_crud(retrieve_name, updated_contacts_list)
            print(retrieve_info)
            which_crud = input("Select another choice by typing it (create, retrieve, update, delete or done): ")
        elif which_crud == 'update':
            update_name = input('Enter the name whose information you want to update: ')
            update_attribute = input(f'Enter the attribute of {update_name} you would like to update: ')
            update_attribute_value = input(f'Enter the value of the {update_attribute} of {update_name} you would like to update: ')
            update_crud(update_name, update_attribute, update_attribute_value, updated_contacts_list)
            update_contacts_list()
            which_crud = input("Select another choice by typing it (create, retrieve, update, delete or done): ")
        elif which_crud == 'delete':
            delete_name = input('Enter the name whose information you want to delete: ')
            delete_crud(delete_name, updated_contacts_list)
            update_contacts_list()
            which_crud = input("Select another choice by typing it (create, retrieve, update, delete or done): ")


main()

    
