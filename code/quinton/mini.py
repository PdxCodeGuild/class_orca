import meals
import webbrowser
import math
from matplotlib import pyplot as plt


gender = input('Enter gender (male/female): ').lower()
age = int(input('Enter age: '))
height = int(input('Enter height in inches: '))
weight = int(input('Enter weight in lbs: '))
goal = input('''What would you say your goal is?\n> 
    1. lose weight
    2. gain weight
''')
amount = int(input('How much? (in lbs)\n> '))

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

if weight > goal_weight:
    end_weeks = weight-goal_weight
else:
    end_weeks = goal_weight-weight

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

print(f'''
Okay. So right now your weight is at {weight}lbs, and your target weight
is {goal_weight}lbs. For that to happen, you need to follow a strict diet
of {bmr:.0f} calories a day.
''')


breakfast_cals = bmr*.40
breakfast_left_over = breakfast_cals%100
breakfast_cals -= breakfast_left_over

lunch_cals = bmr*.33
lunch_left_over = lunch_cals%100
lunch_cals -= lunch_left_over

dinner_cals = bmr*.27
dinner_left_over = dinner_cals%100
dinner_cals -= dinner_left_over

left_over_cals = breakfast_left_over+lunch_left_over+dinner_left_over
left_over_cals = math.floor(left_over_cals)


def meal(calories, dictionary):
    for i in dictionary:
        if calories > 1500:
            meal = dictionary[1500]
        if not i == calories:
            pass
        else:
            meal = dictionary[i]
            return meal
print(f'''
breakfast:\n{meal(breakfast_cals, meals.breakfast_meals)}
''')
print(f'''
lunch:\n{meal(lunch_cals, meals.lunch_meals)}
''')
print(f'''
dinner:\n{meal(dinner_cals, meals.dinner_meals)}
''')
question = input(f'''
All that food and you have {left_over_cals:.0f} calories left! 
Should we search the internet for some good dessert options under {left_over_cals:.0f} calories?\n> ''')
if question == 'yes':
    webbrowser.open('http://www.google.com/search?q=' + 'dessert under ' + str(left_over_cals) + ' calories')

# ----------------------------------------------------- #

plt.style.use('fivethirtyeight')

weeks = [1, end_weeks]

body_weight = [weight, goal_weight]

plt.plot(weeks, body_weight, label='Progress')

plt.xlabel('Week')
plt.ylabel('Bodyweight (lbs)')

plt.title('Bodyweight in (lbs) by Week')

plt.legend()

plt.tight_layout()

plt.show()