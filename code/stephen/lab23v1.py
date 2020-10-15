with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')
    # print(lines)

contacts = []

for line in range(len(lines)):
    keys = lines[0]
    vals = lines[line]
    keys = keys.split(',')
    vals = vals.split(',')
    kvdict = dict(zip(keys, vals))
    contacts.append(kvdict)