# v1
#----------
# meter = float(.3048)
# ft = float(input("Distance in feet?  "))
# print(ft * meter)

# v2
#----------
# ft = float(.3048)
# mi = float(1609.34)
# km = float(1000)

# dist = float(input("Distance?  "))
# unit = input("What Unit? (Ft/Mi/M/KM)  ").lower()
# if unit == 'ft':
#     print(f'{ft * dist} meters')
# elif unit == 'mi':
#     print(f'{mi * dist} meters')
# elif unit == 'm':
#     print(f'{dist} meters')
# elif unit == 'km':
#     print(f'{km * dist} meters')
# else:
#     print("Use valid unit.")

# v3
# ----------
# ft = float(.3048)
# mi = float(1609.34)
# km = float(1000)
# yard = float(.9144) 
# inch = float(.0254)

# dist = float(input("Distance?  "))
# unit = input("What Unit? (Ft/Mi/M/KM/YD/IN)  ").lower()

# if unit == 'ft' or 'feet':
#     print(f'{ft * dist} meters')
# elif unit == 'mi' or 'mile':
#     print(f'{mi * dist} meters')
# elif unit == 'm' or 'meter':
#     print(f'{dist} meters')
# elif unit == 'km' or 'kilometer':
#     print(f'{km * dist} meters')
# elif unit == 'yd' or 'yard':
#     print(f'{yard * dist} meters')
# elif unit == 'in' or 'inch':
#     print(f'{inch * dist} meters')
# else:
#     print("Use valid unit.")

#v4
#back and forth conversion
#----------
ft = float(.3048)
mi = float(1609.34)
km = float(1000)
yard = float(.9144) 
inch = float(.0254)

dist = float(input("Distance?  "))
unit = input("What Unit? (Ft/Mi/M/KM/YD/IN)  ").lower()

if unit == 'ft' or 'feet':
    print(f'{ft * dist} meters')
elif unit == 'mi' or 'mile':
    print(f'{mi * dist} meters')
elif unit == 'm' or 'meter':
    print(f'{dist} meters')
elif unit == 'km' or 'kilometer':
    print(f'{km * dist} meters')
elif unit == 'yd' or 'yard':
    print(f'{yard * dist} meters')
elif unit == 'in' or 'inch':
    print(f'{inch * dist} meters')
else:
    print("Use valid unit.")