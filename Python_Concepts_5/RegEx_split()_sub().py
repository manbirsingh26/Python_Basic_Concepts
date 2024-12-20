import re
"""
Write a program to return a list where the string has split at each whitespace character 
"""
# split()
text = "The 2036 Olympics are happening in India"
x = re.split("\s", text)
print(x)  # It will return a list
# You can control the number of occurrences by specifying the maxsplit parameter:
y = re.split("\s", text, 1)
print(y)

"""
Write a program to replace a match with the string of your choice
"""
# sub()
z = re.sub("\s", "_", text) # It will replace every whitespace character with "_" symbol
print(z)
# We can control the no of occurrences here by specifying the count parameter
result = re.sub("\s", "$", text, 2) # It will replace only first two occurrences of whitespace character
print(result)


