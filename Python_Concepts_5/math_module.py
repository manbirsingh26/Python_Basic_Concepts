"""
Python has a set of built-in math functions, including an extensive math module,
that allows you to perform mathematical tasks on numbers.
There are many functions inside math module , the list of which we can easily find online.
"""
# min and max function
# x = int(input("Enter a number: "))
# y = int(input("Enter a number again: "))
x = 25
y = 30
print(min(x, y))
print(max(x, y))

# The abs() function returns the absolute (positive) value of the specified number:
print(abs(-7.86))

# The pow(x, y) function returns the value of x to the power of y (xy).
print(pow(5, 3))

# Now importing maths module to use extended mathematical functions
import math as m
# The math.sqrt() method for example, returns the square root of a number
x = 64
y = 35
print(m.sqrt(x))
print(m.sqrt(y))

# The math.pi constant, returns the value of PI (3.14...):
print(m.pi)

