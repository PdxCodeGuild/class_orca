distance = int(input("What is the distance? "))

start_units = input('What unit is the distance? (m, mi, ft, km, yd, in) ')
end_units = input('What unit would you like to convert to? (m, mi, ft, km, yd, in) ')

meter_rate = 1
mile_rate = 1609.34
foot_rate = 0.3048
kilometer_rate = 1000
yard_rate = 0.9144
inch_rate = 0.0254

if start_units == 'm':
    conversion_rate_1 = meter_rate
elif start_units == 'mi':
    conversion_rate_1 = mile_rate
elif start_units == 'ft':
    conversion_rate_1 = foot_rate
elif start_units == 'km':
    conversion_rate_1 = kilometer_rate 
elif start_units == 'yd':
    conversion_rate_1 = yard_rate
elif start_units == 'in':
    conversion_rate_1 = inch_rate 
else:
    print('Sorry, you didn\'t enter a valid entry. Please start over')

if end_units == 'm':
    conversion_rate_2 = meter_rate
elif end_units == 'mi':
    conversion_rate_2 = mile_rate
elif end_units == 'ft':
    conversion_rate_2 = foot_rate
elif end_units == 'km':
    conversion_rate_2 = kilometer_rate 
elif end_units == 'yd':
    conversion_rate_2 = yard_rate
elif end_units == 'in':
    conversion_rate_2 = inch_rate 
else:
    print('Sorry, you didn\'t enter a valid entry. Please start over')

end_conversion = conversion_rate_1 * distance / conversion_rate_2

print(f'{distance} {start_units}s is {end_conversion} {end_units}s')

