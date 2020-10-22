# v2
#----------
ft = float(.3048)
mi = float(1609.34)
km = float(1000)

dist = float(input("Distance?  "))
unit = input("What Unit? (Ft/Mi/M/KM)  ").lower()
if unit in ('ft','feet'):
    print(f'{ft * dist} meters')
elif unit in ('mi','mile'):
    print(f'{mi * dist} meters')
elif unit in ('m','meter'):
    print(f'{dist} meters')
elif unit in ('km','kilometer'):
    print(f'{km * dist} meters')
else:
    print("Use valid unit.")