# v3
# ----------
ft = float(.3048)
mi = float(1609.34)
km = float(1000)
yard = float(.9144) 
inch = float(.0254)

while True:
    dist = input("Distance?  ")
    try:
        dist = float(dist)
        break
    except:
        print('Input valid number.')
        dist = input("Distance?  ")

unit = input("What Unit? (Ft/Mi/M/KM/YD/IN)  ").lower()
while True:
    if unit in ("ft", "feet"):
        print(f'{ft * dist} meters')
        break
    elif unit in ('mi','mile'):
        print(f'{mi * dist} meters')
        break
    elif unit in ('m','meter'):
        print(f'{dist} meters')
        break
    elif unit in ('km','kilometer'):
        print(f'{km * dist} meters')
        break
    elif unit in ('yd','yard'):
        print(f'{yard * dist} meters')
        break
    elif unit in ('in','inch'):
        print(f'{inch * dist} meters')
        break
    else:
        print("Re-enter unit.")
        unit = input("What Unit? (Ft/Mi/M/KM/YD/IN)  ").lower()