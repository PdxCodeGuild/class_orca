population = [0, 0] 



def baby_jacks(population):
    # 
    year = 0
    parents = 0
    
    # setting loop to end when population reaches 1000
    while len(population) < 1000:
        
        for i in range (0, len(population), 1):
            population[i] += 1
            # defining parents and floor dividing by population to ensure parents are paired, adding two new pop
            if population[i] >= 4 and population[i] <= 8:
                parents += 1
                if len(population) // parents == 0:
                    population.append(0)
                    population.append(0)
        
        # setting variable for age and removing any jackalopes over 9
        age = population.count(10)
        for i in range(0,age):
            population.remove(10)

        # if population[i] in range(4, 8, 1):
        #     population = [population + [0,0]]
        # adding year to counter
        year += 1
        
        print(year)
        print(population)

baby_jacks(population)
<<<<<<< HEAD
=======

>>>>>>> d08d6b85d2a5e774496b61ebf4b3891ba862148b
