#FIrst Mob lab "jackaloupe"
# By Jo, Ron, and Marc
 
# sets base population of 2 jackalopes
population = [0,0]

def main():

    years = 0

    def age(years):
        global population
        # loops until population is 10000
        while len(population) <= 1000:
            # counts years
            years += 1
            # sets count of fertile rabbits to 0 then adds number of fertile rabbits for that year
            fertile = 0
            for i in population:
                if i >= 4 and i <=8:
                    fertile += 1
            # for each pair of fertile jackalopes appends two new ones to population
            for x in range(0,fertile//2):
                population.append(0)
                population.append(0)
            # ages all jackalopes by one year (adds 1 to each element of list)    
            population = [x + 1 for x in population]
            # removes all dead (10 year old) jackalopes from the population
            population = [x for x in population if x != 10]
        return years

    # assigns function of years to a variable to use output
    total_years = age(years)
    # prints it all out
    print(f'It takes {total_years} years to make 1000 jackalopes')

main()

