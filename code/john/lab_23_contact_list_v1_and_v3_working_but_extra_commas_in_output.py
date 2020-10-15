##############################################################################
# John Fial, PDX Code Guild, 2020-2021
# https://github.com/PdxCodeGuild/class_orca/blob/main/1%20Python/labs/lab23-contact_list.md
##############################################################################

file_to_open = 'contacts.csv' # This line makes it slightly simpler to change the filename

with open(file_to_open, 'r') as file:
    #  = file.read().split('\n')
    contacts_raw = file.read()
    # print(f'contacts_lines is {contacts_lines}')

contacts_lines = contacts_raw.split('\n')

# STEP 2b... Convert each bit (line?) of text into a list inside of a dictionary... a "list of dictionaries," one dict for each user

contacts_list_of_dictionaries = []

def get_csv_headers_line_1(input):
    
    line_number = 1
    header_list = []
    
    for line in input:
        if line_number == 1:
            header_list = line.split(',') # value, though, is a LIST of strings...
            line_number += 1
        else:
            pass
    
    return header_list


def convert_lines_of_strings_with_headers_to_list_of_dictionaries(input):
    
    line_number = 1
    
    for line in input:

        # STRING .split('\n') # https://www.w3schools.com/python/ref_string_split.asp  # is this a for or while function???

        if line_number == 1:  # extract the header line!
            line_number += 1

        else:
            line = line.split(',') # Gives us a list of strings split by comma

            temp_dictionary_entry = {}
            for i in range(len(line)):
                temp_dictionary_entry[header_list[i]] = line[i]        
                # print(temp_dictionary_entry)
            
            contacts_list_of_dictionaries.append(temp_dictionary_entry)        
            line_number += 1

    return contacts_list_of_dictionaries

# Calling functions here:
header_list = get_csv_headers_line_1(contacts_lines)
contacts_list_of_dictionaries = convert_lines_of_strings_with_headers_to_list_of_dictionaries(contacts_lines)

# print(f'contacts_list_of_dictionaries is {contacts_list_of_dictionaries}') # TEST PRINT

# EXAMPLE list
EXAMLE_contacts_list_of_dictionaries = [
    {'name': 'john', 'color': 'clear', 'phone': '503', 'animal': 'penguin'}, 
    {'name': 'josh', 'color': 'red', 'phone': '503', 'animal': 'bat'}, 
    {'name': 'julie', 'color': 'white', 'phone': '310', 'animal': 'cat'}, 
    {'name': 'keenan', 'color': 'green', 'phone': '808', 'animal': 'dog'}
    ]

    # V2 Implement a CRUD REPL...all as functions?
# hints:
    # v2: order of CRUD, best to go in roughly that order when program things...
    # when update or delete.... first step is always retrieve it...
    # write retrieval in function tha you'll use multiple times
    # write to string

    # Step 3 Create a record using input 3a ask for each attribute, save as name_temp, etc... save in dict
    # Step 4 Retreive a record, 4a ask for contact name, 5b print entire dictionary out
    # Step 5 Update a record 5a Ask for contact name, then 5b ask for which attribute to set (if no attribute, ask again), then 5c ask for new value, then 5d re-save list of dicts
    # Step 6 Delete a record 6a Ask user for contact name 6b Remove that contact, 6c ask confirmation
    # Step 10 when finishes (while true? user done?)...








# ***************************** WORKING FROM HERE *****************************
# hint: take a close look at DICT and LIST documents, what methods and functions are helpful there to use?
# hint: think carefully about CSV and what key/values should look like...
# hint for each line in CSV, look at header row, look at key/value





    # STEP 7 CONVERT EACH DICT ITEM BACK TO A STRING...
def convert_back_headers_and_list_of_dictionaries_to_lines_of_strings(input):

    line_number = 1
    output_string = ''

    # FIRST if line #=1, make the output_string first line the header from above, this might be cheating but it's fine..
    if line_number == 1:
        for i in range(len(header_list)):
            output_string += header_list[i] + ',' # NOTE May be problematic, because this is adding a comma to the END of line as well...
            
            # print(output_string)
        line_number += 1
    else:
        pass
    
    # SECOND else, FOR each i in range(len(input)), you want to take the value of each key and add it to the output string
    for temp_dictionary_entry in input: # test range 2 total dictionaries # did NOT want a range... LL!!

        output_string += '\n' # add a new line at the START of each NEW dictionary. #LL DID NOT WORK AT END...
        # Now for each number in header length of values
        for i in range(len(header_list)):
            temp_header_value = header_list[i] # Lookup the header value in the header list
            
            output_string += temp_dictionary_entry[temp_header_value] + ',' # Lookup the header value in the dictionary; Add it io the final csv string with a comma

    
    return output_string



output_string = convert_back_headers_and_list_of_dictionaries_to_lines_of_strings(contacts_list_of_dictionaries)
print(output_string)

##############################################################################
# ***************************** ^^^^^^^^^ TO HERE *****************************

























    # Step 10b Save the list as a new csv "v3 is easier than v1, easier to convert TO csv than v1"
output_file = 'lab23_temp_output_file.txt'
with open(output_file, 'a') as output_file: # changed to 'a' for a safer, append output in testing
    # NOTE The below makes a new line (splits) at the \n character
    output_file.write(output_string)
    # output_file.write('\n'.join(output_string)) # original line...why?
print('    >> PROGRAM ENDED <<    ')
##############################################################################
# https://github.com/PdxCodeGuild/class_orca/blob/main/1%20Python/labs/lab23-contact_list.md
##############################################################################

# Lab 23: Contact List

# Let's build a program to manage a list of contacts. To start, we'll build a CSV ('comma separated values') together, and go over how to load that file. Headers might consist of name, favorite fruit, favorite color. Open the CSV, convert the lines of text into a list of dictionaries, one dictionary for each user. The text in the header represents the keys, the text in the other lines represent the values.

# with open('contacts.csv', 'r') as file:
#     lines = file.read().split('\n')
#     print(lines)

# Once you've processed the file, your list of contacts will look something like this...

# contacts = [
#     {'name':'matthew', 'favorite fruit':'blackberries', 'favorite color':'orange'},
#     {'name':'sam', 'favorite fruit':'pineapple' ...}
# ]

# Note: There is a csv library in Python that will do much of this for you. It is what you would use normally in a project, but for this lab you need to write all the logic yourself.
# Version 2

# Implement a CRUD REPL

#     Create a record: ask the user for each attribute, add a new contact to your contact list with the attributes that the user entered.
#     Retrieve a record: ask the user for the contact's name, find the user with the given name, and display their information
#     Update a record: ask the user for the contact's name, then for which attribute of the user they'd like to update and the value of the attribute they'd like to set.
#     Delete a record: ask the user for the contact's name, remove the contact with the given name from the contact list.

# Version 3

# When REPL loop finishes, write the updated contact info to the CSV file to be saved. I highly recommend saving a backup contacts.csv because you likely won't write it correctly the first time.