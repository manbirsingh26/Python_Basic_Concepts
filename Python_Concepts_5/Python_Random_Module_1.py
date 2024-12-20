import random
#The seed() method is used to initialize the random number generator.
#The random number generator needs a number to start with (a seed value), to be able to generate a random number.
#By default the random number generator uses the current system time.
#If you use the same seed value twice you will get the same random number twice.
random.seed(10)
print(random.random())
print(random.random())



