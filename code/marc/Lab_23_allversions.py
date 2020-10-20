#This is Lab 23. "Contacts list"
# The purpose of this lab is to take a file that is in CSV format, convert it into something
# that you can manipulate in python, then convert it back to a CSV format.

def main():
    with open('contacts.csv', 'r') as file:#this functions opens the original file
        lines = file.read().split('\n')
        # print(lines)
    
    def CSV_to_dict(file): #so every time you open a file you need to run it through here to do anything else with it
        list_of_contacts = [] #blank list to fill with the lists of list from the csv
        for i in range(0, len(file)):#loop to split each item of the csv list into seperate lists 
           list_of_contacts.append(file[i].split(","))#each item in the list is a string that can be conviently split at the comma
        contacts = []#new list of seperate dictionaries
        for i in range(1, len(list_of_contacts)):
            contacts.append(dict(zip(list_of_contacts[0], list_of_contacts[i]))) #combining functions to zip a dictionary together into a new list
        print (list_of_contacts)
        return contacts
    
    def dict_to_CSV (contacts):#This what converts the file back into CSV
        CSV = []
        for name_dict in contacts:
            if list(name_dict.keys()) not in CSV:
                CSV.append(list(name_dict.keys()))
            CSV.append(list(name_dict.values()))
        
        big_list = [item for sublist in CSV for item in sublist]
        print (big_list)
        i = 5
        while i < len(big_list):
           
            big_list.insert(i,("\n" + big_list[i])) #this little bastard was messing things up and it took a long time to figure out why!
            # big_list.remove(big_list[i + 1])
            i += 6
        print (big_list)
        new_file = ",".join(big_list)
        print (new_file)
        
        return new_file

    def add_contact(contacts):#this function adds a new contact
        new_contact = {}
        new_contact['Name'] = (input("What is the contact's name?:\n")).capitalize()
        new_contact['Phone #'] = input("What is the contact's phone # (EX: ###-###-####)?:\n")
        new_contact['Email']  = input("What is the contact's email address?:\n ")
        new_contact['Eye Color'] = input("What is the contact's eye color (or put n/a)?:\n ")
        new_contact['Favorite Band'] = (input("what is the contact's favorite band (or put n/a)?:\n")).title()
        contacts.append(new_contact)
        return contacts
    
    def retrieve_record (contacts):#this function gets a contact from the list
        look_up = "y"
        while look_up == "y":
            what_name = (input("Which contact's info do you need?\n")).capitalize()
            for name_dict in contacts:
                if name_dict["Name"] == what_name:
                    contact_dict = name_dict
                    return contact_dict
         
            look_up = input("Contact not in list, try another?:\n")
            if look_up != "y":
                contact_dict = "No luck"
                break
        
        return contact_dict

    def update_contacts (contacts): #this function allows you to update an existing code
        
        update = "y"
        while update == "y":
            update_contact = (input("Which contact would you like to update?\n")).capitalize()   
            for name_dict in contacts:
                if name_dict["Name"] == update_contact:
                    contact_update = "y"
                    while contact_update == "y":
                        what_attribute = (input("What attribute: 'Name','Phone #', 'Email', 'Eye Color', 'Favorite Band'?\n")).title()
                        if what_attribute in name_dict:
                            if what_attribute == "Name":
                                new_attribute = (input("What is the contact's name?:\n")).capitalize()
                            if what_attribute == 'Phone #':
                                new_attribute = input("What is the contact's phone # (EX: ###-###-####)?:\n")
                            if what_attribute == 'Email':
                                new_attribute = input("What is the contact's email address?:\n")
                            if what_attribute == 'Eye Color':
                                new_attribute = input("What is the contact's eye color (or put n/a)?:\n")
                            if what_attribute == 'Favorite Band':
                                new_attribute = (input("what is the contact's favorite band (or put n/a)?:\n")).title()
                            name_dict [what_attribute] = new_attribute
                            contact_update = input("Change another attribute of this contact:y or no?:\n")
                            if contact_update != "y":
                                break
                else:
                    continue
                 
            update = (input("Do you want to change another contact? y or no?")).lower()
            if update != "y":
                break
        return contacts

    def delete_contacts (contacts): #this function allow you to delete a contact
        delete = "y"
        while delete == "y":
            delete_contact = (input("Which contact would you like to delete?\n")).capitalize()   
            for name_dict in contacts:
                if name_dict["Name"] == delete_contact:
                    contacts.remove(name_dict)
                    break
                else:
                    continue
            delete = (input("Delete someone else? y or n:\n")).lower()
            if delete != "y":
                break
        
        return contacts                                       
    
    contacts = CSV_to_dict(lines)

    # print(list_of_dicts_CSV(contacts))
    
    function_dict = {1:"display all contacts", #this is kind of an underutilized dictionary that I used for organize my thoughts
    2:"add contact",
    3:"update contact",
    4:"delete contact",
    5:"retrieve contact"}
    fixing_contacts = "y"
    while fixing_contacts == "y": #this while loop is my basic interface for the user to choose how they want to manipulate the contacts
        what_function = (input('''What would you like to do?:
"display all contacts"; "update contact"; "add contact";
"delete contact"; or "retrieve contact"?:\n''')).lower()
        if what_function == function_dict[1]:
            print(contacts)
        elif what_function == function_dict[2]:
            add_contact(contacts)
        elif what_function == function_dict[3]:
            update_contacts(contacts)
        elif what_function == function_dict[4]:
            delete_contacts(contacts)
        elif what_function == function_dict[5]:
            retrieve_record(contacts)
        elif what_function not in function_dict: 
            print("Sorry that is not an option.")
            try_again = (input("Try again? y or n:\n")).lower()
            if try_again != "y":
                print(f"Here is your most up-to-date contact list:\n {contacts}")
                break
        fixing_contacts = (input("Do more with contacts? y or n:\n"))
        if fixing_contacts != "y":
            print(f"Here is your most up-to-date contact list:\n {contacts}")
    make_changes = (input("Would you like to save changes? y or n:\n")).lower()
    if make_changes == "y":
        new_file = dict_to_CSV(contacts) 
        with open('contacts.csv', 'w') as file:
            lines = file.write(new_file) #.split('\n') 
            print("\nChanges made!")      
    else:
        print ("\nNo changes made!")
        

main()
