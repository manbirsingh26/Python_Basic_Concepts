"""
4. dict.keys()
5. dict.values()
6. dict.items()
7. pop()
8. popitem()
9. del()
10. fromkeys()
11. copy()
"""
fruits = {
    "Apple": ["Red", 100],
    "Mango": ["Yellow", 120],
    "Kiwi": ["Green", 800],
    "Strawberry": ["Pink", 600],
    "Dragonfuit": ["White", 950],
    "Banana": ["Yellow", 80]
    }
print(fruits.keys())  #Displays all the keys
print(fruits.values())  #Dispalys all the values
print(fruits.items())  #Dispalys all the key-value pairs
fruits.pop("Kiwi")  #Used to delete a key-value by specifying the key
print(fruits)
fruits.popitem()  #Deletes the last item from the dictionary
print(fruits)
del fruits["Mango"]
print(fruits)
# We can also use it to delete the whole dict from the memory
# del fruits
#dict.fromkeys() method returns a dictionary with the specified keys and the specified value
a = ("A", "B", "C")
b = 1
print(dict.fromkeys(a, b))
#Copy() is used to make copy of the dictionary so that we any changes to it are not in original dict
fruits_copy = fruits.copy()
print(fruits_copy)
