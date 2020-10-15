with open('contacts.csv', 'r') as file:
        contents = file.read()

contacts_list = []
lines = contents.split('\n')
keys = lines.pop(0).split(',')
lines_list = [lines[x].split(',') for x in range(len(lines))]


#function to create a dictionary using keys from the first line of the csv file and values from each line after the 
#keys line in the csv file
def add_line_to_contacts_dict(a):
    z = lines_list[a]
    new_dict = {}
    new_dict[keys[0]] = z[0]
    new_dict[keys[1]] = z[1]
    new_dict[keys[2]] = z[2]
    new_dict[keys[3]] = z[3]
    return new_dict


def main():
    for y in range(len(lines_list)):
        contacts_list.append(add_line_to_contacts_dict(y))

    print(contacts_list)

main()

    
