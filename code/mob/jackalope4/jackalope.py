# how long 2 jack takes to make 1000
# jack = 2
# age 4 - 8 they mate
# age 10 they die
# every year + 2 jacks


population = [0,1]    # jackalope population
year = 0    # goes up 1 

while len(population) < 11:
    for jack in population:
        population.insert(jack, + 1)
        print(f'{jack} year old jack')
    # for x in pop > 3 and pop < 9:
    #     pass
    population.append(0) # 2 babies
    population.append(0)

    print(f'{population} is pop')
    year += 1
    print(f'{year} is year')