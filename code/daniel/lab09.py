''
'''
    PDX Code Guild
    Daniel Eggimann
    Lab09
'''

''' Version 1 '''

# gather input from user regarding unit conversion
distance = int(input('Provide a number in feet:  '))
# conversion for feet to meters
ft_to_meter = distance * .3048
# output
print(f'{distance} feet is {ft_to_meter:.4f} meters')


''' Version 2 '''

# gather input to populate 'distance' variable
print('Provide a distance and units to convert to meters.')
distance = input('Distance (enter a numerical digit(s)):  ')

# correct for invalid entries
while not distance.isnumeric(): 
    print('Invalid entry. Please enter a numerical digit(s).')
    distance = input('Distance (enter a numerical digit(s)):  ')
# convert string to integer
distance = int(distance)

orig_units = input('Units (enter "feet", "miles", "meters", "kilometers"):  ')
# correct for invalid entries
while orig_units not in ["feet", "miles", "meters", "kilometers"]:
    print('Invalid entry.')
    orig_units = input('Units (enter "feet", "miles", "meters", "kilometers"):  ')

# conversion chart
ft_to_meter = distance * .3048
mile_to_meter = distance * 1609.34
meter_to_meter = distance * 1
kilometer_to_meter = distance * 1000

# unit conversion logic
if orig_units == 'feet':
    print(f'{distance} {orig_units} is equal to {ft_to_meter:.4f} meters.')
elif orig_units == 'miles':
    print(f'{distance} {orig_units} is equal to {mile_to_meter:.4f} meters.')
elif orig_units == 'meters':
    print(f'{distance} {orig_units} is equal to {meter_to_meter:.4f} meters.')
elif orig_units == 'kilometers':
    print(f'{distance} {orig_units} is equal to {kilometer_to_meter:.4f} meters.')


''' Version 3 '''

# gather input to populate 'distance' variable
print('Provide a distance and units to convert to meters.')
distance = input('Distance (enter a numerical digit(s)):  ')

# correct for invalid entries
while not distance.isnumeric(): 
    print('Invalid entry. Please enter a numerical digit(s).')
    distance = input('Distance (enter a numerical digit(s)):  ')
# convert string to integer
distance = int(distance)

orig_units = input('Units (enter "inches", "feet", "yards", "miles", "meters", "kilometers"):  ')
# correct for invalid entries
while orig_units not in ["inches", "feet", "yards", "miles", "meters", "kilometers"]:
    print('Invalid entry.')
    orig_units = input('Units (enter "inches", "feet", "yards", "miles", "meters", "kilometers"):  ')

# conversion chart
inches_to_meters = distance * 0.0254
ft_to_meter = distance * .3048
yards_to_meters = distance * 0.9144
mile_to_meter = distance * 1609.34
meter_to_meter = distance * 1
kilometer_to_meter = distance * 1000

# unit conversion logic
if orig_units == 'inches':
    print(f'{distance} {orig_units} is equal to {inches_to_meters:.4f} meters.')
elif orig_units == 'feet':
    print(f'{distance} {orig_units} is equal to {ft_to_meter:.4f} meters.')
elif orig_units == 'yards':
    print(f'{distance} {orig_units} is equal to {yards_to_meters:.4f} meters.')
elif orig_units == 'miles':
    print(f'{distance} {orig_units} is equal to {mile_to_meter:.4f} meters.')
elif orig_units == 'meters':
    print(f'{distance} {orig_units} is equal to {meter_to_meter:.4f} meters.')
elif orig_units == 'kilometers':
    print(f'{distance} {orig_units} is equal to {kilometer_to_meter:.4f} meters.')
''

''' Version 4 '''

# gather input to populate 'distance' variable
print('Provide a distance and units for conversion into any other units.')
distance = input('Distance (enter a numerical digit(s)):  ')

# correct for invalid entries
while not distance.isnumeric(): 
    print('Invalid entry. Please enter a numerical digit(s).')
    distance = input('Distance (enter a numerical digit(s)):  ')
# convert string to integer
distance = int(distance)

orig_units = input('Original units for that distance\n(enter inches, feet, yards, miles, meters, kilometers):  ')
# correct for invalid entries
while orig_units not in ["inches", "feet", "yards", "miles", "meters", "kilometers"]:
    print('Invalid entry.')
    orig_units = input('Original units for that distance\n(enter inches, feet, yards, miles, meters, kilometers):  ')

new_units = input('Enter units you would like to convert to:  ')
# correct for invalid entries
while new_units not in ["inches", "feet", "yards", "miles", "meters", "kilometers"]:
    print('Invalid entry.')
    new_units = input('Enter units you would like to convert to.\n(enter inches, feet, yards, miles, meters, kilometers):  ')


# conversion chart
inches_to_meters = distance * 0.0254
ft_to_meter = distance * .3048
yards_to_meters = distance * 0.9144
mile_to_meter = distance * 1609.34
meter_to_meter = distance * 1
kilometer_to_meter = distance * 1000

# convert to meters
if orig_units == 'inches':
    meters = inches_to_meters
elif orig_units == 'feet':
    meters = ft_to_meter
elif orig_units == 'yards':
    meters = yards_to_meters
elif orig_units == 'miles':
    meters = mile_to_meter
elif orig_units == 'meters':
    meters = meter_to_meter
elif orig_units == 'kilometers':
    meters = kilometer_to_meter

# conversion from meters
inches = meters / 0.0254
feet = meters / .3048
yards = meters / .9144
miles = meters / 1609.34
kilometers = meters / 1000

# unit conversion logic
if new_units == 'inches':
    print(f'{distance} {orig_units} is equal to {inches:.4f} {new_units}.')
elif new_units == 'feet':
    print(f'{distance} {orig_units} is equal to {feet:.4f} {new_units}.')
elif new_units == 'yards':
    print(f'{distance} {orig_units} is equal to {yards:.4f} {new_units}.')
elif new_units == 'miles':
    print(f'{distance} {orig_units} is equal to {miles:.4f} {new_units}.')
elif new_units == 'meters':
    print(f'{distance} {orig_units} is equal to {meters:.4f} {new_units}.')
elif new_units == 'kilometers':
    print(f'{distance} {orig_units} is equal to {kilometers:.4f} {new_units}.')

