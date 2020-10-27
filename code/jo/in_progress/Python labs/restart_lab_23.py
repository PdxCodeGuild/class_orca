with open ('contacts.csv', 'r') as file:
    lines = file.read().split("\n")

def create(key,contact):
    for i in key:
        



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

print(contacts_list)

while True:
    crud = input('Would you like to [c]reate, [r]eview, [u]pdate, [d]elete, or [q]uit? ')
    if crud == 'c':
    elif crud == 'r':
    elif crud == 'u':
    elif crud == 'd':
    elif crud == 'q':
        break
    else:
    