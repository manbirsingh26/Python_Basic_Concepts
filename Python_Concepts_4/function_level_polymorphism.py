"""
It means that when a function/method with same name behaves differently for different classes and their objects

# Example of len() function
# for strings
a = "Manbir Singh"
print(len(a))  #It returns the no of characters in the string here 12
# for tuples and lists
b = (2, 3, 4, 6)
print(len(b))  #It returns the total no of items  here 4
# for dict
c = {"Name": "Manbir Singh", "Address": "Jammu"}
print(len(c))  #It returns the total no of key-value pairs  here 2
"""
#Detailed Example using class
#There will be different classes with same method
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def movement(self):
        print(f"Moves!!")

class Yacht:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def movement(self):
        print(f"Sails!")

class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def movement(self):
        print(f"Flies!")

c = Car("Ford", "Mustang GT")
y = Yacht("Lamborghini", "Tecnomar")
p = Plane("Boeing", "BBJ 787")
#Here we can also use for loop directly to print output because we are executing same method for all the classes
for v in (c, y, p):
    print(f"{v.brand} {v.model}")
    v.movement()

