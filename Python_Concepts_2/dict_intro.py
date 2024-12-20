"""
Dictionary:-
1. Ordered Collection of data
2. Stores data in key value pairs
3. It doesn't supports indexing, despite being ordered
4. They are changeable
5. Doesn't allow duplicates
6. Data is accessed using key
7. Iterable
"""
# Creating an empty dictionary
d = {}
d = dict()
# Creating a non-empty dictionary
# First Method
fruits = {
    "Apple": ["Red", 100],
    "Mango": ["Yellow", 120],
    "Kiwi": ["Green", 800],
    "Strawberry": ["Pink", 600],
    "Dragonfuit": ["White", 950],
    "Banana": {"Yellow", 80}
    }
print(fruits)
# Iterating
print("Iterating...")
for key, value in fruits.items():
    print(f"{key}:{value}")

# Second Method
student = dict(Name="Manbir", Class="B.E", RollNo=19, Address="Jammu")
print(student)
# Iterating
print("Iterating...")
for i in student:
    print(f"{i},{student[i]}")

# Third Method
# Using ZIP function
cust = ["Name", "Age", "Profession", "Address"]
details = ["John", 35, "Data Scientist", "35/A,Burn Street, Jammu"]
res = dict(zip(cust, details))
print(res)

# Accessing Data
print(fruits["Kiwi"])
print(student["RollNo"])
print(res["Address"])

# Changeable
# Updating using key
res["Profession"] = "Data Engineer"
fruits["Apple"] = ["Red", {"small": 90, "big": 100}]  # Modifying existing value
student["Stream"] = "Information Technology"  # Adding new value
print(fruits)
print(student)
print(res)



