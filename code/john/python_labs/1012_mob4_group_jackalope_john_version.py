##############################################################################
# Group Lab: Tony, Matthew, and John Fial, PDX Code Guild, 2020-2021
# NEXT STEPS.... DO VERSION 2!! CHANGE THE BIOLOGY!
# https://github.com/PdxCodeGuild/class_orca/blob/main/1%20Python/labs/mob-jackalope.md
##############################################################################


population = [0,0]    # jackalope population
year = 2000    # goes up 1

while len(population) < 1000:

    print(f'{year} is year, START of while loop...')

    # Increase age by 1 for each jack in population
    for i in range(len(population)):
        # print(f'A {age}-year old jack from list {population} ... ')
        # new_age = age
        population[i] += 1
        # print(f'... becomes a {i + 1}-year old jack from list {population}. ')

    year += 1

    # print(f'len(population) is {len(population)} and list is {population}')

    babies = []
    for x in population:
        if x > 3 and x < 9:
            # print(x)
            babies.append(0)

    # print(f'population is {(population)}')

    # Add babies to the main population
    population.extend(babies)
    print(f'len(babies) is {len(babies)} and len(population) is {len(population)}')

    while 11 in population:
        population.remove(11)

    # BELOW WAS THE DUMBER, MORE COMPLICATED WAY to kill off the elders. Worked <200, started to give list index errors greater than 300 or so...
    # for i in range(-1,-len(population),-1):
    #     # print(f'i is {i}')
    #     if population[i] > 10:
    #         population.pop(i)
    #         # population.remove(population[i])

    # print(f'len(population) is {len(population)} and list is {population}')

    print(f'{year} is year, end of while loop...')


# # Final print
print(f'Final len(population) is {len(population)}, and year={year}!')
print('end')


##############################################################################
# https://github.com/PdxCodeGuild/class_orca/blob/main/1%20Python/labs/mob-jackalope.md
##############################################################################
# Mob Programming: Jackalope Simulator
# Version 1

# The goal is to calculate how many years it will take for two jackalopes to create a population of 1000.

#     Jackalopes are reproductive from ages 4-8 and die at age 10.
#     Gestation is instantaneous. Each gestation produces two offspring.
#     Jackalopes are hermaphrodites, it takes a pair to reproduce, but any pair will do

# With these conditions in mind, we can represent our population as a list of ints.
# Version 2

# Now let's give the jackalopes distinct sexes and extend their gestation period to one year. We can represent each jackalope with a dictionary, thus our population will be a list of dictionaries. A jackalope will have the following properties:

#     name
#     age
#     sex
#     whether they're pregnant

# Jackalopes can only mate with those immediately around them. Every generation Jackalopes are randomly shuffled.