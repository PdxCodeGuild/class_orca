#FIrst Mob lab "jackaloupe"
 


population = [0,0]

def main():


    def age():
        fertile = 0
        global population
        while len(population) <= 1000:
            for x in range(fertile):
                population = population.append(0)
            population = [x + 1 for x in population]
            for i in range(len(population)):
                fertile = 0
                if 4 <= population[i] <= 8:
                    fertile += 1
                population = [x for x in population if x !=10]

            

            # 1 fertile removed at 8
            # 1 population  removed at 10
            #     population.append(0)
            #     population.append(0)
        return fertile
        print(fertile)
        print(population)


    


    age()

main()



    
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
    
            # if age >= 4 and age <= 8:
            #     fertile += 1
            # if age == 4:
            #     fertile += 1
            # if age == 8:
            #     fertile -= 1
            # population[i] += 1






