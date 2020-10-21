ft = float(.3048)
mi = float(1609.34)
km = float(1000)
yard = float(.9144) 
inch = float(.0254)

dist = float(input("Distance?  "))
unit = input("Convert what unit? (Ft/Mi/M/KM/Yd/In)  ").lower()

if unit == 'ft':
    temp_dist = dist * ft
elif unit == 'mi':
    temp_dist = dist * mi
elif unit == 'km':
    temp_dist = dist * km
elif unit == 'yd':
    temp_dist = dist * yard
elif unit == 'in':
    temp_dist = dist * inch
elif unit == 'm':
    temp_dist = dist * 1

unit2 = input("To what unit? (Ft/Mi/M/KM/Yd/In) ")

if unit2 == 'ft':
    result = temp_dist / ft
elif unit2 == 'mi':
    result = temp_dist / mi
elif unit2 == 'km':
    result = temp_dist / km
elif unit2 == 'yd':
    result = temp_dist / yard
elif unit2 == 'in':
    result = temp_dist / inch
elif unit2 == 'm':
    result = temp_dist

print(f'{dist} {unit} is equal to {result} {unit2}.')