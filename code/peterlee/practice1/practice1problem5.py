def powers_of_two():
    result = [2**x for x in range(21) ]
    return result

def main():
    powers = powers_of_two()
    print(powers)

main()