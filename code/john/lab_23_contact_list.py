##############################################################################
# John Fial, PDX Code Guild, 2020-2021
# https://github.com/PdxCodeGuild/class_orca/blob/main/1%20Python/labs/lab23-contact_list.md
##############################################################################

file_to_open = 'contacts.csv'

with open(file_to_open, 'r') as file:
    #  = file.read().split('\n')
    contacts_raw = file.read()
    # print(f'contacts_lines is {contacts_lines}')

contacts_lines = contacts_raw.split('\n')

contacts_list_of_dictionaries = []

def next_operation():
    user_input = input(f'Enter next operation: ')
    # user_input = 'create' # TEMP INPUT ### REMEMBER that invalid input here WILL LOOP, which is correct functionality!
    # print(f'LINE 5 user_input is {user_input}')
    return user_input

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


# STEP 2b... Convert each bit (line?) of text into a list inside of a dictionary... a "list of dictionaries," one dict for each user
def input_convert_lines_of_strings_with_headers_to_list_of_dictionaries(input):
    
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

header_list = get_csv_headers_line_1(contacts_lines)

contacts_list_of_dictionaries = input_convert_lines_of_strings_with_headers_to_list_of_dictionaries(contacts_lines)


##############################################################################
# OUTPUT
# STEP 7 CONVERT EACH DICT ITEM BACK TO A STRING...
def output_back_headers_and_list_of_dictionaries_to_lines_of_strings(input):

    line_number = 1
    output_string = ''

    # FIRST if line #=1, make the output_string first line the header from above, this might be cheating but it's fine..
    if line_number == 1:
        # only want the headers added while
        for i in range(len(header_list)): # we only want commas for non-final entries...
            if i != len(header_list)-1:
                output_string += header_list[i] + ',' 
            else:
                output_string += header_list[i]
            # print(output_string)
        line_number += 1
    else:
        pass
    
    # SECOND else, FOR each i in range(len(input)), you want to take the value of each key and add it to the output string
    for temp_dictionary_entry in input: # test range 2 total dictionaries # did NOT want a range... LL!!

        output_string += '\n' # add a new line at the START of each NEW dictionary. #LL DID NOT WORK AT END...

        # Now for each number in header length of values
        for i in range(len(header_list)): # we only want commas for non-final entries...
            if i != len(header_list)-1:
                    
                temp_header_value = header_list[i] # Lookup the header value in the header list
                
                output_string += temp_dictionary_entry[temp_header_value] + ',' # Lookup the header value in the dictionary; Add it io the final csv string with a comma
            else:                    
                temp_header_value = header_list[i] # Lookup the header value in the header list                
                output_string += temp_dictionary_entry[temp_header_value] # Lookup the header value in the dictionary; Add it io the final csv string NO COMMA
    
    output_file = 'lab23_temp_output_file.txt'
    print(f'Saving to file: {output_file}...')
    with open(output_file, 'w') as output_file: # changed to 'a' for a safer, append output in testing
        output_file.write(output_string) # output_file.write('\n'.join(output_string)) # original line...why?


##############################################################################
    # CREATE, RECORD, UPDATE, DELETE
##############################################################################

###### Step 3 Create a record using input 3a ask for each attribute, save as name_temp, etc... save in dict
def create(input_list):
    
    print('Note: does not yet check for duplicate entries, so input carefully!')
    
    new_user_dictionary = {}
    for header in header_list:
        user_input = input(f'Please enter the new entry for \"{header}\", or type \"cancel\" to cancel the new entry: ')
        if user_input == 'cancel':
            print('Cancelling new entry.')
            return
        # user_input = user_input.strip()
        # STEP DISSALLOW COMMAS!!!
        # STEP DISSALLOW COMMAS!!!
        # STEP DISSALLOW COMMAS!!!
        new_user_dictionary[header] = user_input
    input_list.append(new_user_dictionary)
    print(f'Entry added: \"{new_user_dictionary}\".')
    return input_list

##############################################################################
###### Step 4 Retrieve a record: ask the user for the contact's name, find the user with the given name, and display their information
def retrieve(input_list,lookup_name):
    print(f'Looking up input: \"{lookup_name}\"...')
    for temp_dictionary_entry in input_list:
        if lookup_name == temp_dictionary_entry['name']:
            print(f'Contact for input \"{lookup_name}\" found: {temp_dictionary_entry}')
            return temp_dictionary_entry
        else:
            pass
    print(f'No contact information for input: \"{lookup_name}\" found!')
    return False # return something else?





# ***************************** WORKING FROM HERE *****************************

EXAMLE_contacts_list_of_dictionaries = [ # EXAMPLE list
    {'name': 'john', 'color': 'clear', 'phone': '503', 'animal': 'penguin'}, 
    {'name': 'josh', 'color': 'red', 'phone': '503', 'animal': 'bat'}, 
    {'name': 'julie', 'color': 'white', 'phone': '310', 'animal': 'cat'}, 
    {'name': 'keenan', 'color': 'green', 'phone': '808', 'animal': 'dog'}
    ]

##############################################################################
#     # Step 5 Update a record 5a Ask for contact name, then 5b ask for which attribute to set (if no attribute, ask again), then 5c ask for new value, then 5d re-save list of dicts
# def update(input_list):
    
#     print('Note: does not yet check for duplicate entries, so input carefully!')
    
#     new_user_dictionary = {}
#     print(f'Current headers are: {header_list}')

#     for header in header_list:
#         print(f'Current value for header {header} is {header_list}')
    
#         user_input = 

#         new_user_dictionary[header] = user_input



#     return input_list
    

#     # COPY FROM CREATE THEN START...



# print(contacts_list_of_dictionaries)
# update(contacts_list_of_dictionaries)
# print(contacts_list_of_dictionaries)












##############################################################################
# ***************************** ^^^^^^^^^ TO HERE *****************************

##############################################################################
# STEP 6 Delete a record 
def delete(input_list,lookup_name):    

    retrieval_dict = retrieve(input_list,lookup_name)
    
    if retrieval_dict != False: # NOTE FUTURE AND FIGURE OUT Why didn't this work with == True?????
        retrieval_index = input_list.index(retrieval_dict)

        if input_list[retrieval_index] == retrieval_dict:
            print(f'You are deleting the record: \"{lookup_name}\" at position {input_list.index(retrieval_dict)}! Are you sure? For realseys? y/n :') # CHANGE
            # print(input_list)
            del input_list[retrieval_index]
            # print(input_list)
            return input_list # NOTE CHANGED FROM  # CHANGED FROM  # CHANGED FROM  # CHANGED FROM  # CHANGED FROM  # CHANGED FROM contacts_list_of_dictionaries
        else:
            print('else!')
            # run convert_write function (input_list)
            return retrieval_dict
    else: # if False (no user found)
        return


##############################################################################
def main(file):
    print('Welcome to contacts list v1!')
    print(f'Acceptable program inputs are, without quotes: \"create\", \"retrieve\", \"update\", \"delete\", or \"exit\": ')

    # TODO STRIP EXTRA CHARACTERS, LOWERCASE, ETC...

    user_input = next_operation()

    while user_input != 'exit':
        if user_input == 'create':  
            ########### NOTE FIX ENTERING COMMAS AND OTHER DANGEROUS CHARACTERS!
            ########### NOTE FIX ENTERING COMMAS AND OTHER DANGEROUS CHARACTERS!
            ########### NOTE FIX ENTERING COMMAS AND OTHER DANGEROUS CHARACTERS!
            ########### NOTE FIX ENTERING COMMAS AND OTHER DANGEROUS CHARACTERS!
            print('CREATE FUNCTION HERE') # TEMPORARY FOR TESTING 
            create(file)
            output_back_headers_and_list_of_dictionaries_to_lines_of_strings(contacts_list_of_dictionaries) # SAVE OUTPUT
            # user_input = 'exit' # TEMPORARY FOR TESTING
            user_input = next_operation()

        elif user_input == 'retrieve':
            lookup_name = input('Please type the exact name of the entry to display: ')            
            retrieve(file,lookup_name)
            user_input = next_operation()

        elif user_input == 'update':
            ########### NOTE FIX ENTERING COMMAS AND OTHER DANGEROUS CHARACTERS!
            ########### NOTE FIX ENTERING COMMAS AND OTHER DANGEROUS CHARACTERS!
            ########### NOTE FIX ENTERING COMMAS AND OTHER DANGEROUS CHARACTERS!
            ########### NOTE FIX ENTERING COMMAS AND OTHER DANGEROUS CHARACTERS!

            # RUN UPFATE FUNCTION
            # output_back_headers_and_list_of_dictionaries_to_lines_of_strings(contacts_list_of_dictionaries) # SAVE OUTPUT
            print('UPFATE FUNCTION HERE') # TEMPORARY FOR TESTING
            output_back_headers_and_list_of_dictionaries_to_lines_of_strings(contacts_list_of_dictionaries) # SAVE OUTPUT
            # user_input = 'exit' # TEMPORARY FOR TESTING
            user_input = next_operation()

        elif user_input == 'delete':
            lookup_name = input('Please type the exact name of the entry to display: ')
            ########### NOTE FIX ENTERING 'NAME' IN DELETE!
            ########### NOTE FIX ENTERING 'NAME' IN DELETE!
            ########### NOTE FIX ENTERING 'NAME' IN DELETE!
            ########### NOTE FIX ENTERING 'NAME' IN DELETE!
            delete(file,lookup_name)
            output_back_headers_and_list_of_dictionaries_to_lines_of_strings(contacts_list_of_dictionaries) # SAVE OUTPUT
            user_input = next_operation()

        else:            
            print('Invalid input!')
            user_input = next_operation()
            pass

    else: # if user_input is 'exit'...
        print('AFTER WHILE LOOP ELSE Exiting program. Thank you!')
        return file

################# call it!
main(contacts_list_of_dictionaries)
################### FINAL WORK: SAVE TO SAME OPEN FILE
################### FINAL WORK: FIX ENTERING NAME IN DELETE...
################### FINAL WORK: FIX ENTERING COMMAS AND OTHER DANGEROUS CHARACTERS!
# NOTE INPUT 'name' can break whole thing...!
# NOTES 
# return one thing at once
# every time we change / user input, write function... 
# Q add, then update, then delete...
# also if user didn't type exit, it wouldn't save
# FOR EVERY FUNCTION run convert_write function (input_list)



















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