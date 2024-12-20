"""
The keyword "class" is used to create a class
By general convention, we normally start the class name with a capital letter.
Object has all the properties of its class.
"""
"""
Constructor:-
__init__() is called constructor.
All classes have a function called __init__(), which is always executed when the class is being initiated.
Use the __init__() function to assign values to object properties(attributes), or other operations
that are necessary to do when the object is being created.
"""
class Car:
    # Constructor
    def __init__(self, model, brand, year, engine):  # model, brand, etc.. are the attributes of object
        self.model = model
        self.brand = brand
        self.year = year
        self.engine = engine
    # User-defined method
    def output(self):
        print(f"The name of car is {self.model}.It's brand is {self.brand} and year is {self.year}.")

c1 = Car("Mustang", "Ford", 2023, "5 litre naturally aspirated V8")   #Here c1 is object
c1.output()
print(f"Moreover it has {c1.engine}.")


