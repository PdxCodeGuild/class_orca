english = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
    'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

rot_13 = [
    'n', 'o', 'p', 'q',	'r', 's', 't', 'u',	'v', 'w', 'x', 'y', 'z', 'a',
    'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm'
]

user_input = list(input("Please enter a word "))

for letter in user_input:
    if letter in english:
        letter[] = english[]


# print(word[0:25])

position = english.index('p')
position_rot13 = position + 13
# converted = english[position_rot13]
if position_rot13 > 25:
    something = position_rot13 % 13
    # print(something)



# print(position)
#
# print(position_rot13)



# english = [
#     'abcdefghijklmnopqrstuvwzyz'
# ]
#
# rot_13 = [
#     'nopqrstuvwxyzabcdefghijklm'
# ]