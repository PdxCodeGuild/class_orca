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


for i in strings_List:
    if i != ',':
        number_list = ''.join(strings_List)

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




# print("the length of the list is: ", len(number_list))

# print(numbers)

# for i in number_list:
#     if i == '0':
#         digits.append('0)'
#     if i == '1':
#         indexed.append('1)
#     elif i == '2':
#         indexed.append(2)
#     elif i == '3':
#         indexed.append(3)
#     elif i == '4':
#         indexed.append(4)
#     elif i == '5':
#         indexed.append(5)
#     elif i == '6':
#         indexed.append(6)
#     elif i == '7':
#         indexed.append(7)
#     elif i == '8':
#         indexed.append(8)
#     elif i == '9':
#         indexed.append(9)
#     else:
#         indexed.append('\n')
