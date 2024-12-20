import re
# Example
# Do a search that will return a Match Object
txt = "The rain in Spain"
x = re.search("ai", txt)
print(x)   #This will print an object

# Example
# Print the position (start- and end-position) of the first match occurrence.
# The regular expression looks for any words that starts with an upper case "S"
text = "The rain in Spain"
y = re.search(r"\bS\w+", text)
print(y.span())
# The regular expression looks for any words that starts with capital "I" or small "i"
tt = "The New Delhi is the capital of India"
z = re.search(r"\bi\w+", tt, re.IGNORECASE)
print(z.span())

# Example
# Print the string passed into the function
t = "The New Delhi is the capital of India"
a = re.search(r"\bi\w+", t, re.IGNORECASE)
print(a.string)   # This will print the whole string passed to the function

# Example
tx = "The New Delhi is the capital of India"
b = re.search(r"\bI\w+", tx)
print(b.group())   # This will print part of string where match was first found

"""
In each of these methods, "None" is returned if there is no match found
"""



