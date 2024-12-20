"""
List comprehension offers a shorter syntax
when you want to create a new list based on the values of an existing list.
Syntax:-
 newlist = [expression for item in iterable if condition == True]
 """
# Example 1
# Print the squares of all the numbers in a given range in a list
#n = int(input("Enter the range(start is zero): "))
result = [x**2 for x in range(11)]
print(result)

# Example 2
# Make a new list based on the values of an existing list by using a condition
brands = ["audi", "bmw", "porsche", "ducati", "hyundai", "toyota", "mercedes-amg", "kia", "cadillac", "skoda"]
new_list = [x for x in brands if "o" in x]  #Only those names who have "o" in it
new_list1 = [x.capitalize() for x in brands]  #It will create new list by capitalizing all values
new_list2 = [x.replace("kia", "toyota") for x in brands]  #It will replace kis with toyota
#new_list2 = [x if x != "kia" else "toyota" for x in brands]  #It will also replace kis with toyota
new_list3 = [x.upper() for x in sorted(brands)]  # It will create a sorted list based on original list with uppercase
new_list4 = [sum(1 for i in x if i.isalpha()) for x in brands]  # It will print no of characters in each spelling
print(new_list)
print(new_list1)
print(new_list2)
print(new_list3)
print(new_list4)
