import random
import string

population = [
    # {'name': jack_name,
    # 'age': 0,
    # 'sex': jack_sex,
    # 'pregnant': False
    # },

    # {'name': jack_name,
    # 'age': 0,
    # 'sex': jack_sex,
    # 'pregnant': False
    # }
]

def new_jack():

    jack_name = ""
    for x in range(4):
        jack_name += random.choice(string.ascii_lowercase)

    jack_age = 0

    # 0 = female, 1 = male
    jack_sex = random.randint(0,1)

    pregnant = False

    population.append({'name': jack_name, 'age': jack_age, 'sex': jack_sex, 'pregnant': False})

    return jack_name, jack_age, jack_sex, pregnant


print(new_jack())
print(population)


def baby_jacks(population):
    # 
    # year = 0
    # parents = 0

    count = 0
    
    while len(population) < 10:
        for i in range (0, len(population), 1):
            population[i] = [new_jack()]
            for key, value in population:
                population[] += 1



        #     if population[i] >= 4 and population[i] <= 8:
        #         parents += 1
        #         if len(population) // parents == 0:
                    
                    
        # age = population.count(10)
        # for i in range(0,age):
        #     population.remove(10)

        # year += 1
        
        # print(year)

baby_jacks(population)