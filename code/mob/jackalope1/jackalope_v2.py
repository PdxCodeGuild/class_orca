import random
import string


jack_name = ""

for x in range(4):
    jack_name += random.choice(string.ascii_lowercase)
    print(jack_name)

# 0 = female, 1 = male
jack_sex = random.randint(0,1)

population = [
    {'name': jack_name,
    'age': 0,
    'sex': jack_sex,
    'pregnant': False
    }
]

def baby_jacks(population):
    # 
    year = 0
    parents = 0
    
    while len(population) < 1000:
        
        for i in range (0, len(population), 1):
            population[i] += 1
            if population[i] >= 4 and population[i] <= 8:
                parents += 1
                if len(population) // parents == 0:
                    population.append(0)
                    population.append(0)
        
        age = population.count(10)
        for i in range(0,age):
            population.remove(10)

        year += 1
        
        print(year)
        print(population)

baby_jacks(population)