import string
lows = list(string.ascii_lowercase)
uppers = list(string.ascii_uppercase)
numbers = []

for x in range(0,26):
    numbers += [x]
print(numbers)
print(lows)

intake = input('gimme ur secrets  ')
secret = []

for x in intake:
    if x in lows:
        N = lows.index(x)
        N = (N + 13)
        if N > 25:
            N = (N - 26)
        secret += lows[N]
    elif x in uppers:
        N = uppers.index(x)
        N = (N + 13)
        if N > 25:
            N = (N - 26)
        secret += uppers[N]
    else:
        secret += x
print(f'ur secret code is: {"".join(secret)}')