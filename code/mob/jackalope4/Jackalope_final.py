# how long 2 jack takes to make 1000
# jack = 2
# age 4 - 8 they mate
# age 10 they die
# every year + 2 jacks


population = [0, 0]    # jackalope population
year = 0    # goes up 1

while len(population) < 999:
    # print(f'len(population) is {len(population)}')
    # Main code to count adults and add babies
    for x in population:
        if x > 10:
            population.remove(x)
        elif x > 3 and x < 9:
            # print(x)
            population.append(0)
            # print(population)



    # print(year)



    for i in range(len(population)):
        # print(f'A {age}-year old jack from list {population} ... ')
        # new_age = age
        population[i] += 1

        # print(f'... becomes a {i + 1}-year old jack from list {population}. ')


    # Increase age by 1 for each jack in population
    year += 1
    # population.append(0) # Temporary add a baby
    # population.append(0) # Temporary add a baby


    # print(f'{year} is year, end of while loop...')

# # Final print
print(population)
print('end')