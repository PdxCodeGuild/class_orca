# append(population())
# while loop refernceing population item sum 

jackals = [0, 0]
population = len(jackals)
years = 0

# add years to jackals
while population <= 1000:
    for num in range(0, population):
        if num <= 10:
            jackals[num] = jackals[num] + 1
        elif num >10:
            jackals.remove(num)
    print(jackals)


# adding new born jackal
counter = 0
while population <= 1000:
    counter += 1
    for item in jackals:
        if 3 < item <= 10:
            jackals.append(0)
        
print(population)


# def main():
#     # age the population
    # append the population
    # remove deaths

