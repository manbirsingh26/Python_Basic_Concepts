"""
Here child class(derived class) which is derived from parent class(base class),
gets access to all methods and attributes of parent class
Inheritance helps in reusability of code
"""

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
    pass
# If we simply pass statement and don't add any additional method for child class,then it simply
# inherits all the methods and attributes of its parent class
w = Worker("Manbir", "Singh", "Jammu", "B.Tech")
w1 = Worker("Avneet", "Singh", "Indore", "B.Tech")
w2 = Worker("Harleen", "Kour", "Amritsar", "B.Tech")
w.output()
w1.output()
w2.output()
print(f"Total Count: {Person.total_count}")




