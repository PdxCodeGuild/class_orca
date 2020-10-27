distance = float(input("what is the distance? "))

valid_choices = ["ft", "mi", "m", "km", "yd", "inch"]

input_units = input("what are the input units? (in ft/mi/m/km/yd/inch) ")
while input_units not in valid_choices:
    print('That is not a valid choice.')
    input_units = input("what are the input units? (in ft/mi/m/km/yd/inch) ")
else:
    pass

output_units = input("what are the output units? (in ft/mi/m/km/yd/inch) ")
while output_units not in valid_choices:
    print('That is not a valid choice.')
    output_units = input("what are the output units? (in ft/mi/m/km/yd/inch) ")
else:
    pass

if input_units == "ft":
    conversion = distance * 0.3048
elif input_units == "mi":
    conversion = distance * 1609.34
elif input_units == "km":
    conversion = distance * 1000
elif input_units == "yd":
    conversion = distance * 0.9144
elif input_units == "inch":
    conversion = distance * 0.0254
else:
    conversion = distance


if output_units == "ft":
    conversion2 = conversion / 0.3048
elif output_units == "mi":
    conversion2 = conversion / 1609.34
elif output_units == "km":
    conversion2 = conversion / 1000
elif output_units == "yd":
    conversion2 = conversion / 0.9144
elif output_units == "inch":
    conversion2 = conversion / 0.0254
else:
    conversion2 = conversion

print(f"{distance} {input_units} is {conversion2} {output_units}")