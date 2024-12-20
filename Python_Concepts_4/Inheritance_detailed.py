"""
We can add additional methods and properties in the child class
Instead of using "pass" keyword, we can add __init__() function to child class.
When you add the __init__() function, the child class will no longer inherit the parent's __init__() function.

To keep the inheritance of the parent's __init__() function, add a call to the parent's __init__() function
and also mention the names of parameters of parent class which we want to inherit from parents class along
with own parameters of child class

If you add a method in the child class with the same name as a function in the parent class,the inheritance
of the parent method will be overridden.
So always add methods with different name if we don't want to override inheritance of parent method.
"""

# Below is just a simple explanation of inheritance using an imaginary code and methods
# Base class
class Person:
    total_count = 0
    def __init__(self, fname, lname, address, qualification):  # Constructor
        self.fname = fname
        self.lname = lname
        self.address = address
        self.qualification = qualification
        Person.total_count += 1
    # Method(s)
    def output(self):
        print(f"Name:{self.fname} {self.lname}, Address:{self.address}, Qualification:{self.qualification}")
# Child Class
class Worker(Person):
    def __init__(self, fname, lname, address, qualification, designation, resign=True):
        Person.__init__(self, fname, lname, address, qualification)
        #super().__init__(fname, lname, address, qualification) #This is also correct way
        self.designation = designation
        self.resign = resign
    # Adding child class methods
    def new_output(self):
        print(f"Worker name:{self.fname} {self.lname}")
        print(f"Permanent Address:{self.address}")
        print(f"Qualification:{self.qualification}")
        print(f"Designation:{self.designation}")

    def resignation(self):
        if self.resign:
            print(f"{self.fname} {self.lname} has resigned")
            Person.total_count -= 1
            self.resign = False
        else:
            print(f"{self.fname} {self.lname} has already resigned")
w = Worker("Manbir", "Singh", "Jammu", "B.Tech", "Data Analyst")
w1 = Worker("Avneet", "Singh", "Indore", "B.Tech", "Business Analyst")
w2 = Worker("Harleen", "Kour", "Amritsar", "B.Tech", "Data Engineer")
w3 = Worker("Keithrine", "Kour", "Jammu", "B.A", "HRA")
w4 = Worker("Rahul", "Singh", "Delhi", "B.Tech", "Front-End Developer")
w.new_output()
w1.new_output()
w2.new_output()
w3.new_output()
w4.new_output()
print(f"Total Count: {Person.total_count}")
w3.resignation()
w3.resignation()
print(f"Total Count: {Person.total_count}")
w5 = Worker("Varun", "Roy", "Kolkata", "B.Tech", "Debugger")
w5.new_output()
print(f"Total Count: {Person.total_count}")








