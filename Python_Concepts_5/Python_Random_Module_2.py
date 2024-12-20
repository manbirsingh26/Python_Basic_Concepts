import random
#getstate() returns the current internal state of the random number generator
print(random.getstate())

#setstate() restores the internal state of the random number generator
# Example
# Capture and restore the state of the random number generator
print(random.random())  # Print a random (float) number(between 0 and 1)
state = random.getstate() # Capture the state
print(random.random()) # Print another random (float) number(between 0 and 1)
random.setstate(state)  # Restore the state
print(random.random()) # Here the number will be same as when we captured the state
