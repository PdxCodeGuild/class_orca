

#Version 1
def conversion(feet):
    result = feet / 3.28
    return float(result)

feet = float(input("What is the length in feet?  "))
print(conversion(feet))

#Versions 2 & 3
def convert_to_meters(distance, convert_from):

    if convert_from == "feet":
        result = distance * 0.3048
        return float(result)

    elif convert_from == "miles":
        result = distance / 1609
        return float(result)

    elif convert_from == "yards":
        result = distance * .333
        return float(result)

    elif convert_from == "kilometers":
        result = distance * 1000
        return float(result)
    
    elif convert_from == "meters":
        result = distance * 1
        return float(result)
    
    elif convert_from == "inches":
        result = distance * .0254
        return float(result)

distance = float(input("What is the distance?   "))
convert_from = input("What are the units? You can choose feet, yards, miles, or kilometers  ")
print(float(convert_to_meters(distance, convert_from)))

#Version 4
def any_units(distance, convert_to_meters, convert_from, convert_to):

    if convert_to == "feet":
        end_result = float(convert_to_meters(distance, convert_from) * 3.28)
        return float(end_result)
    
    elif convert_to == "miles":
        end_result = float(convert_to_meters(distance, convert_from) * .000621371)
        return float(end_result)
    
    elif convert_to == "kilometers":
        end_result = float(convert_to_meters(distance, convert_from) * .001)
        return float(end_result)
    
    elif convert_to == "meters":
        end_result = float(convert_to_meters(distance, convert_from) * 1)
        return float(end_result)
    
    elif convert_to == "inches":
        end_result = float(convert_to_meters(distance, convert_from) * 39.37)
        return float(end_result)


distance = float(input("What is the distance?   "))
convert_from = input("What are the input units? You can choose feet, meters, yards, miles, or kilometers  ")
convert_to = input("What are the output units? ")
print(float(any_units(distance, convert_to_meters, convert_from, convert_to)))




