"""
Lambda function are used when we need nameless functions for a short period of time.

A lambda function is a small anonymous function.
A lambda function can take any number of arguments, but can only have one expression.

Syntax
lambda arguments : expression
"""

# Adding two numbers using lambda
addition = lambda a, b: a + b
print(addition(5, 10))
print(addition(12, 12.5))

# Greatest number out of three numbers
greater = lambda x, y, z: x if z < x > y else y if z < y > x else z
print(greater(25, 13, 10))
print(greater(12, 13, 10))
print(greater(12, 14, 20))

# Sorting a list according to 2nd sub-element of its elements
l = [(2, 4), (3, 5), (5, 7), (4, 1)]
l.sort()  # It will simply sort according to first sub element of a element
print(l)
#k = lambda ele: ele[1]
#l.sort(key=k)  # It will sort according to second sub-element of a element
l.sort(key=lambda ele: ele[1])  #Doing it in a short way
print(l)
