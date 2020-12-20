# Day 2 of Advent of code 2020

# 1-3 a: abcde
# 1-3 b: cdefg
# 2-9 c: ccccccccc
# Each line gives the password policy and then the password.
# The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid.
# For example, 1-3 a means that the password must contain a at least 1 time and at most 3 times.

# In the above example, 2 passwords are valid. The middle password, cdefg, is not;
# it contains no instances of b, but needs at least 1. The first and third passwords are valid:
# they contain one a or nine c, both within the limits of their respective policies.

# How many passwords are valid according to their policies?

number_of_matches = 0

string_list = []

first_num = []
first_num_for_conversion = ''
string_of_first_list = []

second_num = []
second_num_for_conversion = ''
second_list_strings = []

key_letter = []
key_string = []

password_letters = []
password_list = []

end_program = 'false'

letter_value = []
alphabet_list = [
    ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
]
number_list = [
    ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
]

with open('day_2.txt', 'r') as get_file:
    contents = get_file.read()

# change contents from one long string, to multiple strings beggining where '\n' was
split_contents = contents.split('\n')
# print(split_contents)

contents_counter = 0

length_of_contents = len(split_contents)
# print(length_of_contents)
while end_program == 'false':
    for x in range(length_of_contents):
        # print(split_contents[0])
        for i in split_contents[contents_counter]:
            string_list.append(i)
        # print(sting_list)
        # print(f' Counter is {contents_counter}')
        # print(split_contents[contents_counter])

        contents_counter += 1

        # print(f' Counter is {contents_counter}')
        # print(split_contents[contents_counter])

        # First number section to isolate number as an int
        first_num.append(string_list[0])
        first_num.append(string_list[1])
        # print('------------------')
        # print(first_num)
        first_list_strings = []
        for i in first_num:
            if i in str(number_list):
                if i != '-':
                    first_list_strings.append(i)
        # print(first_list_strings)

        first_num_for_conversion = ''
        for i in first_list_strings:
            first_num_for_conversion += str(i) + ""
        first_number_int = int(first_num_for_conversion)
        # print(f'First number: {first_number_int}')
        # if first_num[0] in str(alphabet_list)

        # Second number section to isolate number as an int

        second_num.append(string_list[2])
        second_num.append(string_list[3])
        second_num.append(string_list[4])

        second_list_strings = []

        for i in second_num:
            if i in str(number_list):
                if i != ' ':
                    second_list_strings.append(i)
        # print(string_of_second_list)

        second_num_for_conversion = ''
        # convert example: '1' '5'  to   '15'
        for i in second_list_strings:
            second_num_for_conversion += str(i) + ""

        # second number is now ready as an int
        second_number_int = int(second_num_for_conversion)
        # print(f'Second number: {second_number_int} ')

        # Section to isolate the key letter

        if string_list[4] in str(alphabet_list):
            key_letter.append(string_list[4])
        if string_list[5] in str(alphabet_list):
            key_letter.append(string_list[5])
        if string_list[6] in str(alphabet_list):
            key_letter.append(string_list[6])

        # remove the ' ' from the list

        for i in key_letter:
            if i != ' ':
                key_string.append(i)
        # print(f'key letter is {key_string}')

        for i in key_string:
            key = i
        # print(f'Key letter: {key}')


        # print(string_list)
        len_counter = 7
        while True:
            if len_counter >= len(string_list):
                break
            elif string_list[len_counter] in str(alphabet_list):
                    password_list.append(string_list[len_counter])
                    len_counter += 1
            elif string_list[7] == ':':
                len_counter += 1
                password_list.append(string_list[len_counter])

        # print(password_list)

        key_counter = 0

        for i in password_list:
            if i == key:
                key_counter += 1
        # print(key_counter)

        if key_counter >= first_number_int:
            if key_counter <= second_number_int:
                number_of_matches += 1
        # print(key)
        # print(password_list)

        string_list.clear()
        first_num.clear()
        # print(first_num)
        # first_num_for_conversion.clear()
        string_of_first_list.clear()

        second_num.clear()
        # second_num_for_conversion.clear()
        second_list_strings.clear()

        key_letter.clear()
        key_string.clear()

        password_letters.clear()
        password_list.clear()

        letter_value.clear()
    print(f'Number of matches {number_of_matches}')
    end_program = 'true'