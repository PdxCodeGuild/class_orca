with open('contacts.csv', 'r') as file:
    lines = file.read().split('\n')

contact_dict = []

header = lines[0].split(',')
h_len = len(header)
lines.pop(0)
lines_sans_commencement = []
print(lines)
for b in lines:
    print(b.split(','))
for x in lines:
    lines_sans_commencement += x.split(',')
print(lines_sans_commencement)

# for y in range(h_len):
#     for z in lines_sans_commencement[y::h_len]:
#         contact_dict.append({header[y]:z})

print(contact_dict)

#############
# with open('contacts.csv', 'w') as file:
#     lines = file.write('stuff here')