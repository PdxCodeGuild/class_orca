""" once v1 works, will modify rotation to be iditable """


# function to encrypt message
def encrypt():
    global message
    message = [x.upper() for x in message]
    encrypted = [english[i] for i in message]
    encrypted = [rot13[i] for i in encrypted]
    return encrypted


# english cipher dict
english = {
    "A": 0,
    "B": 1,
    "C": 2,
    "D": 3,
    "E": 4,
    "F": 5,
    "G": 6,
    "H": 7,
    "I": 8,
    "J": 9,
    "K": 10,
    "L": 11,
    "M": 12,
    "N": 13,
    "O": 14,
    "P": 15,
    "Q": 16,
    "R": 17,
    "S": 18,
    "T": 19,
    "U": 20,
    "V": 21,
    "W": 23,
    "X": 24,
    "Y": 25,
    "Z": 26
}

# asks user which way they want to run the cipher
action = input("Would you like to encrypt or decrypt? ")
rot = input("What rotation would you like to use?")

# will pick which function to run based on input. loops back if entry is invalid
while True:
    if action == "encrypt":
        message = input("What is the message you would like to encrypt? ")
        message = list(message)
        print(encrypt())
        break
    elif action == "decrypt":
        message = input("What is the message you would like to decrypt? ")
        message = list(message)
        print(decrypt())
        break
    elif action != "encrypt" or "decrypt":
            print("Please try again with an appropriate entry.\n")
            action = input("Would you like to encrypt or decrypt? ")




""" 
don't think i'll need this

# ROT13 cipher dict
rot13 = {
    0: "N",
    1: "O",
    2: "P",
    3: "Q",
    4: "R",
    5: "S",
    6: "T",
    7: "U",
    8: "V",
    9: "W",
    10: "X",
    11: "Y",
    12: "Z",
    13: "A",
    14: "B",
    15: "C",
    16: "D",
    17: "E",
    18: "F",
    19: "G",
    20: "H",
    21: "I",
    23: "J",
    24: "K",
    25: "L",
    26: "M"
} """

""" 
ignoring for now

# function to decrypt a message
def decrypt():
    global message
    message = [x.upper() for x in message]
    decrypted = [rot13[i] for i in message]
    decrypted = [english[i] for i in message]
    return decrypted """
