# Traditional Method
a = input("Enter a string: ")
n = len(a)
for i in range(n-1, -1, -1):
    print(a[i], end="")

# Shortcut Method using Slicing
a = input("Enter a string: ")
print(a[::-1])
