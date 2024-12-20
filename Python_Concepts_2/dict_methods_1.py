"""
Dictionary supports the following methods:-
1. len()
2. get()
3. update()
"""

fruit_colour = {
    "Apple": ["Red", 100],
    "Mango": ["Yellow", 120],
    "Kiwi": ["Green", 800],
    "Strawberry": ["Pink", 600],
    "Dragonfuit": ["White", 950],
    "Banana": ["Yellow", 80]
    }
print(fruit_colour)
print(len(fruit_colour))
print(fruit_colour.get("Strawberry"))  #get() is used to access the values of dictionary using keys
#print(fruit_colour.get("Guava"))  #is case value is not present, it doesn't throws error, it simply returns "None"
print(fruit_colour.get("Guava", "No Data Available"))  #we can also write custom message for keys
#not present in our dictionary
# Updating using key
fruit_colour["Cherry"] = ["Crimson", 400]  # Adding a new value
fruit_colour["Banana"] = ["Yellow", {"Small": 60, "Big": 80}]  # Updating existing value
# Updating  using update()
fruit_colour.update({"Papaya": ["Parrot", 150]})  # Adding new value
fruit_colour.update({"Mango": ["Yellow", 105]})  #update() to update the values of dict and doesn't returns the list
print(fruit_colour)
a = {"A": 1, "B": 2, "C": 3}
b = {"D": 4, "E": 5, "F": 6}
a.update(b)  # update() method is also used to add merge one dict with another one
print(a)



