

# function to encrypt message
def encrypt():
    global message
    message = [x.upper() for x in message]
    encrypted = [english[i] for i in message]
    encrypted = [rot13[i] for i in encrypted]
    return encrypted

# function to decrypt a message
def decrypt():
    global message
    message = [x.upper() for x in message]
    decrypted = [rot13_d[i] for i in message]
    decrypted = [english_d[i] for i in decrypted]
    return decrypted

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
}
# english dycrypt cypher
english_d = {
    0: "A",
    1: "B",
    2: "C",
    3: "D",
    4: "E",
    5: "F",
    6: "G",
    7: "H",
    8: "I",
    9: "J",
    10: "K",
    11: "L",
    12: "M",
    13: "N",
    14: "O",
    15: "P",
    16: "Q",
    17: "R",
    18: "S",
    19: "T",
    20: "U",
    21: "V",
    23: "W",
    24: "X",
    25: "Y",
    26: "Z"
}
# rot13 dycrypt cypher
rot13_d = {
    "N": 0,
    "O": 1,
    "P": 2,
    "Q": 3,
    "R": 4,
    "S": 5,
    "T": 6,
    "U": 7,
    "V": 8,
    "W": 9,
    "X": 10,
    "Y": 11,
    "Z": 12,
    "A": 13,
    "B": 14,
    "C": 15,
    "D": 16,
    "E": 17,
    "F": 18,
    "G": 19,
    "H": 20,
    "I": 21,
    "J": 23,
    "K": 24,
    "L": 25,
    "M": 26
}
action = input("Would you like to encrypt or decrypt? ")

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


