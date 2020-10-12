# how long 2 jack takes to make 1000
# jack = 2
# age 4 - 8 they mate
# age 10 they die
# every year + 2 jacks


population = [0,0]    # jackalope population
year = 0    # goes up 1 

while len(population) < 11:
    print(f'len(population) is {len(population)}')
    # Main code to count adults and add babies
    # for x in pop > 3 and pop < 9:
    #     pass

    # population.append(0) # 2 babies

    # print(f'{population} is pop')


    # Increase age by 1 for each jack in population
    year += 1
    population.append(0) # Temporary add a baby

    for age in population:
        print(f'Line 27 for a {age}-year old jack')
        new_age = age
        population.remove(age)
        new_age += 1
        population.append(new_age)
        print(f'Line 32 for a {age}-year old jack')
        print(population)

    print(f'{year} is year, end of while loop...')

print(population)
print('end')