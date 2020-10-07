'''
Lab 9: Unit Converter
Version 1
Matthew Chimenti
'''

# # as the user to enter a number the wish to covert
# number_feet = int(input("What is the number of feet you wish to convert? "))
# #convert the number into meters
# number_meters = number_feet * 0.3048
#
# #print the feet into meters
# print(f"{number_feet} ft is {number_meters} m")

'''
Version 2
'''

    # 'km': 1000,
    # 'm': 1,
    # 'mi': 1609.34,
    # 'ft': .3048,


# # ask the user to select which unit they would like to covert
# unit_selection = input("Which unit would like like to convert? 'km' 'm' 'mi' or 'ft' ")
# number = int(input(f'How many {unit_selection} would you like to convert? '))
#
# # go through the conditional of km
# if unit_selection == 'km':
#     answer = number * 1000
#     print(f'{number} km is {answer} meters ')
#
# # go through the conditional of m
# elif unit_selection == 'm':
#     answer = number * 1
#     print(f'{number} m is {answer} meters ')
#
# # go through the conditional of mi
# elif unit_selection == 'mi':
#     answer = number * 1609.34
#     print(f'{number} mi is {answer} meters ')
#
# # go through the conditional of ft
# elif unit_selection == 'ft':
#     answer = number * .3048
#     print(f'{number} ft is {answer} meters ')
#
# # if user does not make a valid selection, inform then
# else:
#     print("You did not make a valid selection")

'''
Version 3
'''

# # ask the user to select which unit they would like to covert into a variable
# unit_selection = input("Which unit would like like to convert? 'km' 'm' 'mi' 'ft' 'yd' or 'inch' ")
# # make a variable for the number of units they want to convert
# number = int(input(f'How many {unit_selection} would you like to convert? '))
#
# # go through the conditional of km
# if unit_selection == 'km':
#     answer = number * 1000
#     print(f'{number} km is {answer} meters ')
#
# # go through the conditional of m
# elif unit_selection == 'm':
#     answer = number * 1
#     print(f'{number} m is {answer} meters ')
#
# # go through the conditional of mi
# elif unit_selection == 'mi':
#     answer = number * 1609.34
#     print(f'{number} mi is {answer} meters ')
#
# # go through the conditional of ft
# elif unit_selection == 'ft':
#     answer = number * .3048
#     print(f'{number} ft is {answer} meters ')
#
# # go through the conditional of yd
# elif unit_selection == 'yd':
#     answer = number * .9144
#     print(f'{number} ft is {answer} meters ')
#
# # go through the conditional of inch
# elif unit_selection == 'inch':
#     answer = number * .0254
#     print(f'{number} ft is {answer} meters ')
#
# # if user does not make a valid selection, inform then
# else:
#     print("You did not make a valid selection")

'''
Version 4
'''

# get the input for distance and two units we will convert
distance = int(input('What is the distance? '))
first_unit = input('What is the input units? ')
second_unit = input('What is the output units? ')

# convert the first_unit into meters
if first_unit == 'km':
    meters = distance * 1000

if first_unit == 'mi':
    meters = distance * 1609.34

if first_unit == 'm':
    meters = distance * 1

if first_unit == 'ft':
    meters = distance * .3048

if first_unit == 'yd':
    meters = distance * .9144

if first_unit == 'inch':
    meters = distance * .0254


# convert the second_unit into meters
if second_unit == 'km':
    answer = meters / 1000

if second_unit == 'mi':
    answer = meters / 1609.34

if second_unit == 'm':
    answer = meters / 1

if second_unit == 'ft':
    answer = meters / .3048

if second_unit == 'yd':
    answer = meters / .9144

if second_unit == 'inch':
    answer = meters / .0254

# calculate the converted units from meters into the answer and print
print(f"{distance} {first_unit} is {answer} {second_unit}")


