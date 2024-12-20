import functools

# print(dir(functools))  #It shows names of all functions in functools package.
"""
reduce() is contained inside "functools" module of Python
reduce(): apply a function to an iterable and reduce it to a single cumulative value
          It applies function to the first two elements and repeats process until one value remains
syntax:
reduce(function, iterable)
"""
# Example1
# Take a list as an input and display all the elements as a single string
letters = ["K", "A", "W", "A", "S", "K", "I"]
# reduce() function requires two variables(elements) as input
result = functools.reduce(lambda i, j, : i + j, letters)
print(result)

# Example2
# Take a list of  numbers and find the multiple of all numbers
number = [5, 4, 3, 2, 1]
res = functools.reduce(lambda i, j, : i*j, number)
print(res)
