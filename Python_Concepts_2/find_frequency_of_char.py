"""
Find frequency of each character in a string and print the following:
> character:frequency
"""
x = input("Enter your string: ")
result = {}
for i in x:
    key = i
    value = x.count(i)
    result[key] = value
print(result)
#or
"""
for i in x:
    result[i] = x.count(i)
print(result)
"""
