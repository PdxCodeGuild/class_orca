# importing everything I need
import meals
import webbrowser
import math
from matplotlib import pyplot as plt
# grabbing all information from user
name = input('Enter name: ')
gender = input('Enter gender (male/female): ').lower()
age = int(input('Enter age: '))
height = int(input('Enter height in inches: '))
weight = int(input('Enter weight in lbs: '))
goal = input('''What would you say your goal is?\n> 
    1. lose weight
    2. gain weight
''')
amount = int(input('How much? (in lbs)\n> '))
# if/else statements to figure out female or male and lose weight or gain weight
if goal == '1':
    goal_weight = weight-amount
    if gender == 'male':
        bmr = 66 + (6.23*(goal_weight)) + (12.7*height) - (6.8*age)
    else:
        bmr = 655 + (4.35*(goal_weight)) + (4.7*height) - (4.7*age)
else:
    goal_weight = weight+amount
    if gender == 'male':
        bmr = 66 + (6.23*(goal_weight)) + (12.7*height) - (6.8*age)
    else:
        bmr = 655 + (4.35*(goal_weight)) + (4.7*height) - (4.7*age)
# how many weeks your diet will be
if weight > goal_weight:
    end_weeks = weight-goal_weight
else:
    end_weeks = goal_weight-weight
# getting the users activity level and multiplying it to find your batal metabolic rate
activity_level = input('''
What would you say your activity level is?
    1. sedentary (little or no exercise)
    2. lightly active (light exercise 1-3 days a week)
    3. moderately active (moderate exercise 3-5 days a week)
    4. very active (hard exercise 5 or more days a week)
> ''')
if activity_level == '1':
    bmr *= 1.2
elif activity_level == '2':
    bmr *= 1.375
elif activity_level == '3':
    bmr *= 1.55
elif activity_level == '4':
    bmr *= 1.725
# nice print message to explain things to user
print(f'''
Okay {name}. So right now your weight is at {weight}lbs, and your target weight
is {goal_weight}lbs. For that to happen, you need to follow a strict diet
of {bmr:.0f} calories a day.
''')
# multiplying to find calories per meal
breakfast_cals = bmr*.40
breakfast_left_over = breakfast_cals%100
breakfast_cals -= breakfast_left_over

lunch_cals = bmr*.33
lunch_left_over = lunch_cals%100
lunch_cals -= lunch_left_over

dinner_cals = bmr*.27
dinner_left_over = dinner_cals%100
dinner_cals -= dinner_left_over
# left over calories for desert
left_over_cals = breakfast_left_over+lunch_left_over+dinner_left_over
left_over_cals = round(left_over_cals)

# grabbing different meals from the list in meals.py
def meal(calories, dictionary):
    for i in dictionary:
        if calories > 1500:
            meal = dictionary[1500]
        if not i == calories:
            pass
        else:
            meal = dictionary[i]
            return meal
# printing out breakfast lunch and dinner
print(f'''
breakfast:\n{meal(breakfast_cals, meals.breakfast_meals)}
''')
print(f'''
lunch:\n{meal(lunch_cals, meals.lunch_meals)}
''')
print(f'''
dinner:\n{meal(dinner_cals, meals.dinner_meals)}
''')
# searching the web for a dessert under the left over calories
question = input(f'''
All that food and you have {left_over_cals:.0f} calories left! 
Should we search the internet for some good dessert options under {left_over_cals:.0f} calories?\n> ''')
if question == 'yes':
    webbrowser.open('http://www.google.com/search?q=' + 'dessert under ' + str(left_over_cals) + ' calories')
else:
    pass

# ----------------------------------------------------- #
# printing out a progress chart to show where you should be by each week
plt.style.use('fivethirtyeight')

weeks = [0, end_weeks]

body_weight = [weight, goal_weight]

plt.plot(weeks, body_weight, label='Progress')

plt.xlabel('Week')
plt.ylabel('Bodyweight (lbs)')

plt.title('Bodyweight in (lbs) by Week')

plt.legend()

plt.tight_layout()

plt.show()
#---------------#
# pie chart to show the caloric break down of each meal
plt.style.use('fivethirtyeight')

slices = [breakfast_cals, lunch_cals, dinner_cals, left_over_cals]
labels = [f'Breakfast\n{int(breakfast_cals)} cals', f'Lunch\n{int(lunch_cals)} cals', f'Dinner\n{int(dinner_cals)} cals', f'Desert\n{left_over_cals} cals']
colors = ['#008fd5', '#fc4f30', '#e5ae37', '#6d904f']

plt.pie(slices, labels=labels, colors=colors,
         wedgeprops={'edgecolor': 'black'})

plt.title(f'Total Calories:\n{bmr:.0f} cals')
plt.tight_layout()
plt.show()