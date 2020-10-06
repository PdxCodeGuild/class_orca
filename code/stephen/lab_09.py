print('Welcome to the Unit Converter!')

unit1 = input('''What is the input unit of measure you would like to convert?
ft for feet, mi for miles, km for kilometer or m for meters:
>''')
dist = int(input('''What is the amount of input units you would like to convert?
>'''))
unit2 = input('''What is the output unit of measure you would like to convert?
ft for feet, mi for miles, km for kilometer or m for meters:
>''')
units = ['ft', 'mi', 'm', 'km']
while unit1 != units:
    print('''Invalid selection! 
Please select ft for feet, mi for miles, km for kilometer or m for meters:''')
    unit1 = input('''What is the input unit of measure you would like to convert?
ft for feet, mi for miles, km for kilometer or m for meters:
>''')
    break
while unit2 != units:
    print('''Invalid selection! 
Please select ft for feet, mi for miles, km for kilometer or m for meters''')
    unit2 = input('''What is the output unit of measure you would like to convert?
ft for feet, mi for miles, km for kilometer or m for meters:
>''')
    break

while unit1 == 'ft':
    if unit2 == 'm':
        total = dist * 0.3048
        print(f'{dist} {unit1} is {total:.2f}{unit2}s!')
        break
    if unit2 == 'mi':
        total = dist / 5280
        print(f'{dist} {unit1} is {total:.2f}{unit2}s!')
        break
    if unit2 == 'km':
        total = dist / 3280
        print(f'{dist} {unit1} is {total:.2f}{unit2}s!')
        break
while unit1 == 'm':
    if unit2 == 'ft':
        total = dist / 0.3048
        print(f'{dist} {unit1} is {total:.2f}{unit2}!')
        break
    if unit2 == 'mi':
        total = dist / 1609.34
        print(f'{dist} {unit1} is {total:.2f}{unit2}s!')
        break
    if unit2 == 'km':
        total = dist / 1000
        print(f'{dist} {unit1} is {total:.2f}{unit2}s!')
        break
while unit1 == 'mi':
    if unit2 == 'm':
        total = dist * 1609.34
        print(f'{dist} {unit1} is {total:.2f}{unit2}s!')
        break
    if unit2 == 'ft':
        total = dist * 5280
        print(f'{dist} {unit1} is {total:.2f}{unit2}!')
        break
    if unit2 == 'km':
        total = dist * .621371
        print(f'{dist} {unit1} is {total:.2f}{unit2}s!')
        break
while unit1 == 'km':
    if unit2 == 'm':
        total = dist * 1000
        print(f'{dist} {unit1} is {total:.2f}{unit2}s!')
        break
    if unit2 == 'ft':
        total = dist * 3280
        print(f'{dist} {unit1} is {total:.2f}{unit2}!')
        break
    if unit2 == 'mi':
        total = dist * .621371
        print(f'{dist} {unit1} is {total:.2f}{unit2}s!')
        break
    


    
