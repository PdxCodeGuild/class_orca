##############################################################################
# John Fial, PDX Code Guild, 2020
# use meters as an intermediary, convert input to meters, then convert again to 
##############################################################################

welcome = 'Welcome to Unit Converter! Currently only the following inputs and outputs are accepted: m, km, ft, mi, in, and yd'
print(welcome)

user_distance = input('Please enter the numerical distance, without units: ') # FIX, as this is easy to break with a non-numerical input
user_distance = float(user_distance)

user_input = input('Please enter your input units, exactly as written above: ')
user_output = input('Please enter your output units, exactly as written above: ')

# Convert their input to meters 
if user_input == 'm':
    distance_in_meters = user_distance * 1 
elif user_input == 'km':
    distance_in_meters = user_distance * 1000
elif user_input == 'ft':
    distance_in_meters = user_distance * 0.3048
elif user_input == 'mi':
    distance_in_meters = user_distance * 1609.34
elif user_input == 'in':
    distance_in_meters = user_distance * 0.0254
elif user_input == 'yd':
    distance_in_meters = user_distance * 0.9144
else:
    distance_in_meters = 0
    print('error in user input!') # FIX, so that nothing can break this section
    
# Convert their input in meters to their desired output units
if user_output == 'm':
    result = distance_in_meters / 1
elif user_output == 'km':
    result = distance_in_meters / 1000
elif user_output == 'ft':
    result = distance_in_meters / 0.3048
elif user_output == 'mi':
    result = distance_in_meters / 1609.34
elif user_output == 'in':
    result = distance_in_meters / 0.0254
elif user_output == 'yd':
    result = distance_in_meters / 0.9144
else:
    result = 0
    print('error in user output!') # FIX, so that nothing can break this section
    
# Final print result
print(f'{user_distance} {user_input} = {result} {user_output}') 


##############################################################################
# copied lab from programming 102 lab #3 below, using dictionaries:
##############################################################################
'''
units = {
    # LEGEND: 'unit_name':'distance_in_meters',
    'm':1, #meters
    'ft':0.3048, #feet
    'mi':1609.34, #miles
    'km':1000, #kilometers
    'yd':0.9144, #yards
    'in':0.0254, #inches
    }

welcome = 'Welcome to Unit Converter! Current output is always m. Inputs accepted: m, km, ft, mi, in, and yd'
print(welcome)

input_distance = input('Please enter the numerical distance, without units: ')
input_distance = float(input_distance)

input_conversion = input('Please enter your input units, exactly as written above: ')

# I don't just overwrite their input with the key value, because I want to print it soon...
conversion_factor = input_conversion
conversion_factor = units.get(conversion_factor, f'ERROR: Lookup of unit name {conversion_factor} failed...') # CHANGE

result = input_distance * conversion_factor
print(f'{input_distance} {input_conversion} = {result} m') 
'''
