import matplotlib.pyplot as plt

#for bar graph
import numpy as np

print("""Hello and Welcome to Calorie Targeter

We must collect some information in order to estimate your caloric intake. After which, 
we will enter it into the revised Harris Benedict Equation and provide you the results.""")


print()
gender = input("Let us being by first asking what is your gender? male or female ")
weight_kilo = int(input("What is your weight in pounds? "))
cm_height = int(input("How tall are you in inches? "))
age = int(input("What is your age? "))

# convert weight and height to pounds and feet
weight = weight_kilo / 2.205
height = cm_height * 2.54
# print(weight)
# print(height)

# allow the user to identify their activity level
exercise_level = int(input("""
What is  your exercise level, 1-5 
1 Sedentary: little or no regular exercise 
2 Mild : intensive exercise for at least 20 minuets, 1 to 3 times a week
3 Moderate: intensive exercise for at least 30 to 60 minutes 3 to 4 times weekly
4 Heavy: intensive exercise for 60 minuets or greater 5 to 7 days weekly
5 Extreme: Exceedingly active and or very demanding activities.  
"""))


if gender == 'male':
    total_calories_needed = 0
    # (REVISED) HARRIS BENEDICT EQUATIONS:
    bmr = 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    # print(bmr)

    # Activity or stress factors
    if exercise_level == 5:
        total_calories_needed = bmr * 1.9
    elif exercise_level == 4:
        total_calories_needed = bmr * 1.7
    elif exercise_level == 3:
        total_calories_needed = bmr * 1.5
    elif exercise_level == 2:
        total_calories_needed = bmr * 1.3
    elif exercise_level == 1:
        total_calories_needed = bmr * 1.2

elif gender == 'female':
    # (REVISED) HARRIS BENEDICT EQUATIONS:
    bmr = 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    # print(bmr)

    # Activity or stress factors
    if exercise_level == 5:
        total_calories_needed = bmr * 1.9
    elif exercise_level == 4:
        total_calories_needed = bmr * 1.725
    elif exercise_level == 3:
        total_calories_needed = bmr * 1.55
    elif exercise_level == 2:
        total_calories_needed = bmr * 1.375
    elif exercise_level == 1:
        total_calories_needed = bmr * 1.2

high_weight_loss = total_calories_needed * .71
standard_weight_loss = total_calories_needed * .85
mild_weight_loss = total_calories_needed * .9
maintain = total_calories_needed * 1
bulking = total_calories_needed + 250

# print(f"""
# Consume the following target amount of calories for your goal
#
# 1 Bulk, weight gain: {round(bulking,2)} calories
# 2 Maintain  weight: {round(total_calories_needed,2)} calories
# 3 Mild weight loss: {round(mild_weight_loss,2)} calories
# 4 Standard weight loss: {round(standard_weight_loss,2)} calories
# 5 High weight loss: {round(extreme_weight_loss, 2)} calories
# """)

weight_goal = int(input("""What is your weight loss/weight gain goal?""
1: High weight loss:
2: Standard weight loss
3: Mild weight loss
4: Maintain weight
5: Bulk
"""))
if weight_goal == 1:
    total_calories_needed = high_weight_loss
elif weight_goal == 2:
    total_calories_needed = standard_weight_loss
elif weight_goal == 3:
    total_calories_needed = mild_weight_loss
elif weight_goal == 4:
    total_calories_needed = maintain
elif weight_goal == 5:
    total_calories_needed = bulking


consumed_today = int(input("Lastly, how many calories have you had today? "))
# num = int(input("number?"))


calories_needed_math = total_calories_needed - consumed_today
print(f'''
In order to meet your caloric intake goal, you need to consume 
{round(calories_needed_math, 2)} more calories today
''')
print("Please refer to the following graphs for visualization.")
# ==============================================================================
# Graph section

fig, ax = plt.subplots(figsize=(10, 10))

# Graph the data
# X axis
x = [1, 2, 3, 4, 5]
# Y axis
y = [high_weight_loss, standard_weight_loss, mild_weight_loss, maintain, bulking]


plt.yticks([100, 200, 300, 400, 500, 600, 700, 800, 900,
            1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900,
            2000, 2100, 2200, 2300, 2400, 2500, 2600, 2700, 2800, 2900,
            3000, 3100, 3200, 3300, 3400, 3500, 3600, 3700, 3800, 3900,
            4000, 4100, 4200, 4300, 4400, 4500, 4600, 4700, 4800, 4900])



plt.plot(x, y, color="dodgerblue", label='Target Calories', linewidth=8)
plt.plot([x], [y], marker='o', markersize=8, color="black")





# Plot dot of
x2 = [weight_goal]
y2 = [consumed_today]
plt.plot([x2], [y2], marker='X', markersize=20, color="red", label='Current Calories For Weight Goal')



# Graph title
plt.title('Calories Needed For Exercise Level')
plt.legend()
# Add grid lines
plt.grid(True)
# Labels y axis
plt.ylabel('Calories')
# Labels x axis
plt.xlabel('Weight Goal')
# X axis metrics/label
labels = ['High Weight Loss', 'Standard Weight loss', 'Mild Weight Loss', 'Maintain', 'Bulk']
plt.xticks(x, labels)

# Start and stop point for arrows made into variables
xy_arrowy = total_calories_needed - 50
xytext_arrowy = consumed_today + 50

# Arrow section
ax.annotate("",
            # Arrow head
            xy=(weight_goal, xy_arrowy), xycoords='data',
            # Arrow base
            xytext=(weight_goal, xytext_arrowy), textcoords='data',
            # Curved arrow
            size=40, va="center", ha="center",
            arrowprops=dict(arrowstyle="simple",
                            color="red",
                            connectionstyle="arc3,rad=-0.1"),
            )

# Auto Wrapping text

t = (f"Consume {round(calories_needed_math, 2)} more calories today to meet your daily Goal")
plt.text(weight_goal, xy_arrowy - 300, t, fontsize=14, family='serif', style='italic', ha='left', rotation=-15, wrap=True)

# Makes the graph show
plt.show()
plt.axis([0, 5, 0, 4000])

# Bar graph
#=============================================================================================

labels = ['Hight Weight Loss', 'Standard Weight loss', 'Mild Weight Loss', 'Maintain', 'Bulk']
calories_consumed = [consumed_today, consumed_today, consumed_today, consumed_today, consumed_today]
calories_needed = [round(high_weight_loss, 1), round(standard_weight_loss, 1), round(mild_weight_loss, 1), round(maintain, 1), round(bulking, 1)]

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/2, calories_consumed, width, label='Consumed Calories')
rects2 = ax.bar(x + width/2, calories_needed, width, label='Needed Calories')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Calories')
ax.set_title('Calories Needed For Exercise Level')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()


def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)
autolabel(rects2)

fig.tight_layout()

plt.show()