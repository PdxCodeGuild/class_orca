#FIrst Mob lab "jackaloupe"
 


population = [4,4]

def main():


    def age():

        fertile = 0
        for i, age in enumerate(population):
            # if age >= 4 and age <= 8:
            #     fertile += 1
            if age == 4:
                fertile += 1
            if age == 8:
                fertile -= 1
            population[i] += 1
            #     population.append(0)
            #     population.append(0)
        # return fertile
        print(fertile)
        print(population)
    
    for i in range(len(population)):
        if 4 <= population[i] <= 8:
            fertile = True
    


    age()




    
    # def jackaloupe_breeding_mach(jacks):
    #     years = 0
    #     while jacks < 1000:
    #         years += 1
    #         for age in range(10):

    #             if 4 >= age <= 8:
    #                 jacks += 2
    #             if age >= 10:
    #                 jacks -= 1
    #             print(jacks)
    #     return years


    # for age in range(10):

    # print(jackaloupe_breeding_mach(2))
    







main()