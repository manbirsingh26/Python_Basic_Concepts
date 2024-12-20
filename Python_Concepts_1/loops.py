# While Loop Example
lis = ("Harleen", "Manbir", "Avneet", "Palakpreet")
i = 0
while i < 4:
    print(lis[i])  # we can also use "end" keyword here to print them in a single line
    i += 1

# For loop example
lis = ("Harleen", "Manbir", "Avneet", "Palakpreet")
for i in range(0, len(lis)):
    print(lis[i])

# Print all even numbers from 0 to 20
for i in range(0, 21):
    if i % 2 == 0:
        print(i, end=" ")

# Print the sum of numbers in the given range
a = int(input("Enter start of range: "))
b = int(input("Enter end of range: "))
sumation = 0
for i in range(a, b+1):
    sumation = sumation + i
print(sumation)

# Use of Jump keyword in range(start, end-1, jump)
for i in range(1, 11, 2):
    print(i, end=" ")


