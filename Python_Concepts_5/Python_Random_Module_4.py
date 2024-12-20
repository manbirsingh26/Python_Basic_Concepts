import random
a = [10, 20, 30, 40, 50, 60, 70]
random.shuffle(a)  # Takes a sequence and shuffles the sequence in a random order
print(a)

print(random.sample(a, k=5)) # It will contain randomly selected 5 elements from the given list(k =< size of list)

print(random.uniform(5, 7))# It returns a random float number between the given two parameters
# Similar method
# triangular(low,high, mode = Midpoint(Default)
# The mode parameter gives you the opportunity to weigh the possible outcome closer
# to one of the other two parameter values.
print(random.triangular(1, 10, 7))  # Here the random no will most likely be closer to 10


