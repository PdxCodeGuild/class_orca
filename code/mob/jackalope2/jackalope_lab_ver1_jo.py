#FIrst Mob lab "jackaloupe"
 


population = [0,0]

def main():

    years = 0
    def age(years):
        global population
        # appends list with 0 for new jackalopes (fertile) 
        while len(population) <= 1000:
            print(years)
            years += 1
            fertile = 0
            for i in population:
                if i >= 4 and i <=8:
                    fertile += 1
            for x in range(0,fertile//2):
                population.append(0)
                population.append(0)
            # ages all jackalopes by one year (adds 1 to each element of list)    
            population = [x + 1 for x in population]
            # finds total number of fertile rabbits and adds to fertile
            population = [x for x in population if x != 10]
        print(years)
        return years

    total_years = age(years)
    print(f'It takes {total_years} years to make 1000 jackalopes')

main()







