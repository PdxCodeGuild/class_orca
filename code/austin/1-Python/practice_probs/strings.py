#Practice problems - Strings

import random

# #1
# def double_letters(x):
#     this_string = ""
#     doubled_string = [i * 2 for i in x]
#     for char in doubled_string:
#         this_string += char
#     return this_string
# print(double_letters('hello'))

# #2
# def rando_erase(string):
#     new_list = []
#     for char in string:
#         i = random.randint(0, len(string) -1)
#         # print(i)
#         # print(string[i])
#         new_string = string.replace(string[i], "")
#         new_list.append(new_string)
#     print(new_list)

# rando_erase("chilaquiles")

#3 
def latest_letter(string):
    string_list = list(string)
    string_list.sort()
    latest_letter = string_list[len(string_list) -1]

    print(f"The latest letter is: {latest_letter}")

latest_letter('erjlkewjrluwerljlkdjf')



