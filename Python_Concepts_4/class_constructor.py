"""
"Constructor" is a special method which is used to create and initialize object of a class.
Name of method/function:    __init__()
It is defined in the class.
It is automatically executed at the time of object creation.
It has a self parameter which is a reference to the current instance of the class,
and is used to access variables that belongs to the class.
"""
class Person:
    # Constructor
    def __init__(self, name, age, address, gender):
        self.name = name
        self.age = age
        self.address = address
        self.gender = gender
p = Person("Manbir", 22, "Jammu & Kashmir", "Male")
p1 = Person("Naman", 23, "Jammu & Kashmir", "Female")
# p and p1 are objects of class Person
print(f"Name:{p.name}")
print(f"Age:{p.age}")
print(f"Address:{p.address}")
print(f"Gender:{p.gender}")
print(f"Name:{p1.name}")
print(f"Age:{p1.age}")
print(f"Address:{p1.address}")
print(f"Gender:{p1.gender}")
