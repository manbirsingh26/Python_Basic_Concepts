"""
It means when a same operator behaves differently for different kinds of inputs
"""
# Example of + operator
class Addition:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def add(self):
        print(f"Addition of entered two nos is:{self.a+self.b}")

class Concatenation:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def concat(self):
        print(f"Concatenation of entered two strings is:{self.x+self.y}")

a = Addition(25, 45)
a1 = Addition(25.5, 45.6)
c = Concatenation("Manbir", "Singh")
c1 = Concatenation("20", "02")
a.add()
a1.add()
c.concat()
c1.concat()
# In output we can see how + operator is behaving differently in case of numerical and string inputs


