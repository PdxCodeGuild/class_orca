

# *'-.-'*'-.-'*'-.-'*-.-'*-.-'*-.-'*-.-'*'-.-'*'-.-'*'-.-'*
#        Project: Python
# Assignment/Ver: Lab09
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

units = {
"ft": .3048,        # meters in a foot
"m": 1,             # meters in a meter
"km": 1000,         # meters in a kilometer
"mi": 1609.34,      # meters in a mile
"yd": 0.9144,       # meters in a yard
"in": 0.0254        # meters in a inch
}

#----Functions----------------------------------------------

def ver_1():
    ''' Version 1 '''

    # Input
    print('\n*** Convert feet to meters ***\n')
    in_feet = input('What is the distance in feet: ')
    in_feet = float(in_feet)

    # Logic
    in_meters = in_feet * units["ft"]

    # Result
    print(f'\n{in_feet} ft is {in_meters:.2f} m\n')


def ver_2():
    ''' Version 2 & 3 '''

    # Input
    print('\n*** Convert a chosen unit to meters ***')
    distance = input('\nWhat is the distance: ')

    # Data validation practice (needs try and accept!)
    # if distance != distance.isnumeric():
    #     print('Invalid selection')
    #     distance = input('\nWhat is the distance: ')
    
    distance = float(distance)
    unit = input('\nWhat is the unit (ft, m, km, mi, yd, or in): ')

    # Data validation
    valid_input = ['ft', 'm', 'km', 'mi', 'yd', 'in']
    while unit not in valid_input:
        print('Invalid selection!')
        unit = input('\nWhat is the unit (ft, m, km, mi, yd, or in): ')

    # Logic 
    in_meters = distance * units[unit]

    # Result
    print(f'\n{distance} {unit} is {in_meters:.2f} m\n')


def ver_4():
    ''' Version 4 '''
    # Note: Did not build with user validation/error checking

   # Intro
    print('''
\n*** Convert a unit distance to another unit distance ***
               (ft, m, km, mi, yd, or in)

''')
    # Input
    distance = input('\t\tWhat is the distance:  ')
    input_units = input('\t\tWhat are the input units: ')
    output_units = input('\t\tWhat are the output units: ')
    distance = float(distance)

    # Unit conversion & evaluation
    to_meters = distance * units[input_units]
    from_meters = round(to_meters / units[output_units])

    # Result
    print(f'\n\t\t *** {distance} {input_units} is {from_meters} {output_units} ***')

#--------Main Code---------------------------------------------

def main():
    ''' User input for version '''

    version = ''
    while version != ('1', '2', '4', 'exit'):
        version = input('\nWhich version? (1, 2, 4 or exit): ')
        if version == '1':
            ver_1()
        elif version == '2':
            print(" ** Version 2 and 3")
            ver_2()
        elif version == '4':
            ver_4()
        elif version == 'exit':
            break
        else:
            print('>>> Invalid selection\n')
            continue
main()

#----End Code--------------------------------------------------
