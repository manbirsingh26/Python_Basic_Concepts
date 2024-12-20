import random
# getrandbits() method returns an integer in the specified size (in bits)
print(random.getrandbits(8)) # This will return a random 8 bits-sized integer(e.g 10010011 -> 147)
print(random.getrandbits(6)) # This will return a random  6 bits-sized integer

# randint(a, b) returns the random number(int) between the given range (both included).
print(random.randint(1, 100))
print(random.randint(500, 1000))

# randrange(a, b) also returns a random number between the given range( b not included)
print(random.randrange(2, 6))

# choice() returns a random element from the given sequence(list, tuple, set)
a = ["Manbir", "Naman", "Avneet", "Kashmir", "Harleen", "Sam"]
print(random.choice(a))

# choices(sequence, weights=None, cum_weights=None, k=1)
# Returns a list with a random selection from the given sequence
b = ["Apple", "Banana", "Mango", "Dragonfruit", "Orange", "Radish", "Pomegranate"]
print(random.choices(b, k=12)) #Equal selection possibility of all elements
print(random.choices(b, weights=[3, 1, 1, 1, 1, 1, 1], k=12)) #Three times higher possibility of selection of "Apple"
# as compared to others



