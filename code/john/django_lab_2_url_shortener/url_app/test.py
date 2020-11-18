# LAB 2, URL SHORTENER. NAMES: URL_PROJECT AND URL_APP.

import string
import random

characters = string.digits + string.ascii_letters # + string.ascii_uppercase

code = ''

while len(code) < 8:
    next_character = random.choice(characters)
    code += next_character

else:
    print(f'Your code is: \n{code}')