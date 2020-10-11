# This is  Lab 13 ver 2 (allows for user to choose encryption)
# Write a program that prompts the user for a string, and encodes it with ROTchoice. For each character, find the corresponding character, add it to an output string. Notice that there are 26 letters in the English language, so encryption is the same as decryption.

def main():
    def rot_coder(x, a, y = "e"):
        alphabet = {0:"a", 1:"b", 2:"c",
        3:"d",
        4:"e",
        5:"f",
        6:"g",
        7:"h",
        8:"i",
        9:"j",
        10:"k",
        11:"l",
        12:"m",
        13:"n",
        14:"o",
        15:"p",
        16:"q",
        17:"r",
        18:"s",
        19:"t",
        20:"u",
        21:"v",
        22:"w",
        23:"x",
        24:"y",
        25:"z"}

        alpha_num_value = {"a":0, "b":1, "c":2,
        "d":3,
        "e":4,
        "f":5,
        "g":6,
        "h":7,
        "i":8,
        "j":9,
        "k":10,
        "l":11,
        "m":12,
        "n":13,
        "o":14,
        "p":15,
        "q":16,
        "r":17,
        "s":18,
        "t":19,
        "u":20,
        "v":21,
        "w":22,
        "x":23,
        "y":24,
        "z":25}
        original_list = list(x.lower()) 
        convert_list = []

        if y == "e":
            for char in original_list:
                if char in alpha_num_value:
                    num_char = alpha_num_value [char]
                    if (num_char + a) < 26:
                        code_char = alphabet [(num_char + a)]  
                    if (num_char + a) >=26:
                        code_char = alphabet [((num_char + a) - 26)] 
                else:
                    code_char = char 
                convert_list.append(code_char) 
            coded_string = ''.join(convert_list)
        if y == "d":
            for char in original_list:
                if char in alpha_num_value:
                    num_char = alpha_num_value [char]
                    if (num_char - a) >= 0:
                        code_char = alphabet [(num_char - a)]  
                    if (num_char - a) < 0:
                        code_char = alphabet [((num_char - a) + 26)] 
                else:
                    code_char = char 
                convert_list.append(code_char) 
            coded_string = ''.join(convert_list)
        return coded_string
       
    to_be_encoded = input("Enter the the word or phase you want to encode:\n")
   
    y = input("Would you like to encode(e) or decode(d)?:\n") 
    while y != "e" and y != "d":
        y = input("e or d?")
    
    how_much = int(input("By how much rotation, 1 - 26?:\n")) 
    while how_much < 0 or how_much > 26:
         how_much = int(input("By how much rotation, 1 - 26?:\n")) 
    
    print(rot_coder(to_be_encoded, how_much, y))
main()


