unus = {
    1: "I",
    2: "II",
    3: "III",
    4: "IV",
    5: "V",
    6: "VI",
    7: "VII",
    8: "VIII",
    9: "IX"
}

decem = {
    1: "X",
    2: "XX",
    3: "XXX",
    4: "XL",
    5: "L",
    6: "LI",
    7: "LII",
    8: "LIII",
    9: "IC"
}

centi = {
    1: "C",
    2: "CC",
    3: "CCC",
    4: "CD",
    5: "D",
    6: "DC",
    7: "DCC",
    8: "DCCC",
    9: "CM"
}


number = input('Enter your number to convert: ')

split_number = list(number)
if len(split_number) == 3:
    ones = unus[int(split_number[2])]
    tens = decem[int(split_number[1])]
    hundreds = centi[int(split_number[0])]
    print(f'{hundreds}{tens}{ones}')
elif len(split_number) == 2:
    ones = unus[int(split_number[1])]
    tens = decem[int(split_number[0])]
    print(f'{tens}{ones}')
else:
    ones = unus[int(split_number[0])]
    print(f'{ones}')




