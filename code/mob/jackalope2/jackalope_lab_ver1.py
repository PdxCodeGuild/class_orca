#FIrst Mob lab "jackaloupe"
 


population = [8,8]

def main():
    
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

    

    def age():

        fertile = 0
        for i, age in enumerate(population):
            population[i] += 1
            if age >= 4 and age <= 8:
                fertile += 1
            #     population.append(0)
            #     population.append(0)
        # return fertile
        print(fertile)
        print(population)
    
    age()




    # print(jackaloupe_breeding_mach(2))
    







main()