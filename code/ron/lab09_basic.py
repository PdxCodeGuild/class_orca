

# *'-.-'*'-.-'*'-.-'*-.-'*-.-'*-.-'*-.-'*'-.-'*'-.-'*'-.-'*
#        Project: Python
# Assignment/Ver: Lab09_basic
#         Author: Ron Mansolilli, ron.mansolilli@gmail.com
#           Date: 10-03-2020
# *'-.-'*'-.-'*'-.-'*-.-'*-.-'*-.-'*-.-'*'-.-'*'-.-'*'-.-'*

#----Instructions and notes-----------------------------------------
''' 

Unit Converter

'''
#----Modules------------------------------------------------

''' none '''

#----Global variables, lists, dictionaries------------------

''' none '''

#----Functions----------------------------------------------

''' none '''

#--------Main Code---------------------------------------------

''' Version 1 '''

# User Input
print("\nVersion 1")
print("----------")

user_input = float(input('What is the distance in feet: '))

# Logic & output
distance = user_input * .3048
print(f'\n {user_input} ft is {distance:.2f} m')

''' Version 2 & 3 '''

print("\nVersion 2 & 3")
print("----------")

# User Input
user_distance = float(input('What is the distance: '))
user_units = input('What are the units: ')

# Logic
if user_units == 'ft':
    distance = user_distance * .3048
elif user_units == 'mi':
    distance = user_distance * 1609.34
elif user_units == 'km':
    distance = user_distance * 1000
elif user_units == 'yd':
    distance = user_distance * .9144
elif user_units == 'in':
    distance = user_distance * .0254
elif user_units == 'm':
    distance = user_distance * 1
    # else:
    #     print('Invalid selection')

# Output
print(f'\n {user_distance} {user_units} is {distance:.2f} m')

''' Version 4 '''

print("\nVersion 4")
print("----------")

# User Input
user_distance = float(input('What is the distance: '))
user_units = input('What are the input units: ')
user_outputs = input('What are the output units: ')

# Logic
if user_units == 'ft':
    distance = user_distance * .3048
elif user_units == 'mi':
    to_meters = user_distance * 1609.34
elif user_units == 'km':
    to_meters = user_distance * 1000
elif user_units == 'yd':
    to_meters = user_distance * .9144
elif user_units == 'in':
    to_meters = user_distance * .0254
elif user_units == 'm':
    to_meters = user_distance * 1

if user_outputs == 'ft':
    distance = to_meters / .3048
elif user_outputs == 'mi':
    distance = to_meters / 1609.34
elif user_outputs == 'km':
    distance = to_meters / 1000
elif user_outputs == 'yd':
    distance = to_meters / .9144
elif user_outputs == 'in':
    distance = to_meters / .0254
elif user_outputs == 'm':
    distance = to_meters / 1

# Output
print(f'\n {user_distance} {user_units} is {distance} {user_outputs}\n')







#----End Code--------------------------------------------------
