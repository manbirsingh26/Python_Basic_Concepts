"""
Given a list of population census, find the total number of population
Each value in the list represents total no of members in a family
"""
cen = [4, 7, 7, 9, 1, 3, 5, 3, 7, 4, 4, 6, 5, 5]
result = [sum(x for x in cen)]
print(f"Total population turns out to be:{result}")
# Another way:
"""
pop = 0
for i in cen:
    pop += i
print(f"Total population turns out to be: {pop}")
"""
