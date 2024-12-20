"""
The math.fsum() method returns the sum of all items in any iterable (tuples, arrays, lists, etc.).
Syntax: math.fsum(iterable)
If the iterable is not numbers, it returns a TypeError
"""
import math
print(math.fsum([12, 35.5, 23, 5.8]))
print(math.fsum((12, 34, 2.8, 15.3)))