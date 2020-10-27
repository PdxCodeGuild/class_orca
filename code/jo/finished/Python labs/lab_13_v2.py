
# function to encrypt message. takes the list message and adds the rot value to pull from rotated dictionary
def encrypt():
    global message
    global rot
    message = [x.upper() for x in message]
    encrypted = [english[i] for i in message]
    encrypted = [rotated[i + rot] for i in encrypted]
    return encrypted

# function to decrypt a message. does same thing but subtracts the rot value
def decrypt():
    global message
    global rot
    message = [x.upper() for x in message]
    decrypted = [english[i] for i in message]
    decrypted = [rotated[i - rot] for i in decrypted]
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
    "W": 22,
    "X": 23,
    "Y": 24,
    "Z": 25
}
# reversed key:value dictionary
rotated = {
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
     22: "W",
     23: "X",
     24: "Y",
     25: "Z"
}

# asks user which way they want to run the cipher
action = input("Would you like to encrypt or decrypt? ")
# gets to rotation value and reduces it to a number useable in the dictionaries
rot = int(input("What cypher rotation would you like to use? "))
if rot > 26:
    rot = rot // 26

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


