# '''
# PDX Code Guild
# Daniel Eggimann & Quinton Baseman
# Jackalope Lab
# '''
# jackals = [0, 0]
# years = 0

# while len(jackals) <= 1000:
#     for num in range(len(jackals)):
        
#         # living jackals
#         if jackals[num] <= 9:
#             # age the jackal by one year
#             jackals[num] = jackals[num] + 1
#             # # birthing jackals
#             if 4 <= jackals[num] <= 8:
#                 jackals.append(0)

#         # removing dead jackals
#         elif jackals[num] == 10:
#             jackals.remove(jackals[num])
    
#     # time pass
#     years += 1
    

# print(years)
# print(len(jackals))
'''jackalope_num = 1
jackals = [
    {
    'name': 'jackalope_'(jackalope_num),
    'age': 0,
    'sex': 'm',
    'pregnant': 'no'
    },
    {
    'name': 'jackalope_2',
    'age': 0,
    'sex': 'f',
    'pregnant': 'no'
    }
]
years = 0

while len(jackals) <= 1000:
    for dictionary in jackals:
        # living jackals
        if dictionary['age'] <= 9:
            # 'age' the jackal by one year
            dictionary['age'] = dictionary['age'] + 1
            # # birthing jackals
            if 4 <= dictionary['age'] <= 8:
                jackals.append(0)

        # removing dead jackals
        elif jackals[dictionary['age']] == 10:
            jackals.remove(jackals[dictionary['age']])
    
    # time pass
    years += 1
    

print(years)
print(len(jackals))

'''
