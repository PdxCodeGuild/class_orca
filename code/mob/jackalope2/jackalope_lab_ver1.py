#FIrst Mob lab "jackaloupe"
 
def main():
    
    def jackaloupe_breeding_mach(jacks):
        years = 0
        while jacks < 1000:
            
            years += 1
            for age in range(10):

                if 4 >= age <= 8:
                    jacks += 2
                if age >= 10:
                    jacks -= 1
                print(jacks)
        return years
           
    print(jackaloupe_breeding_mach(2))
    







main()