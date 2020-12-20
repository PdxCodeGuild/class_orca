strings_List = []
number_list = []
removed_list = []
ready_list = []


with open('data.txt', 'r') as get_file:
    contents = get_file.read()


#covert list into items into one long string with ',' instead of '\n'
for i in contents:
    if i == '\n':
        strings_List.append(',')
    else:
        strings_List.append(i)
print(strings_List)

for i in strings_List:
    if i == ',':
        number_list = ''.join(strings_List)
print(number_list)

removed_list = number_list.split(',')
# print(removed_list)

for i in removed_list:
    conv_num = int(i)
    ready_list.append(conv_num)
print(ready_list)

i = 0
x = 0
while True:

    if int(removed_list[i]) + int(removed_list[x]) == 2020:
        print(f"the sum of {int(removed_list[i])} + {int(removed_list[x])} is 2020")
        break
        # print(x)

    else:
        # print(f'{int(removed_list[i]) + int(removed_list[x])}')
        # print(i)
        i += 1
        if i == 199:
            x += 1
            i = 0



