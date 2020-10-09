import string

#creates a table to convert the string into
letters_list = list(string.ascii_lowercase)

#the function that does the string conversion
def ROT(a):
    new_index = letters_list.index(a)
    #chances the encryption based on user input
    converted_index = new_index + asked_amount
    if converted_index > 25:
        converted_index -= 26
    return letters_list[converted_index]

asked_string = input("Enter a string in lower-case letters: ")
#creates a variable to shift the encryption
asked_amount = int(input("How much rotation would you like to use in the encryption? "))

#splits the string into a list for convenience
string_list = list(asked_string)

#performs the conversion and puts the characters in a list
converted_list = [ROT(a) for a in string_list]

#joins the characters in the converted list to create the output string
converted_string = ''.join(converted_list)

print(f'The ROT conversion is {converted_string}')




