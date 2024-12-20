import re
"""
Write a program to check if a string starts with "The" and ends with "India"
"""
# search()
text = "The New Delhi is the capital of India"
x = re.search('^The.*India$', text)
if x:
    print(f"Yes! It is a match")
else:
    print(f"No Match!")

"""
Write a program to print the list of all substrings(matches) which satisfy the condition
"""
# findall()
txt = "The rain in Spain can't go in vain"
y = re.findall("ai", txt)
z = re.findall("India", txt)
print(y)
print(z)  # Here it will return empty list as there is no match

"""
Write a program to search for first-whitespace character in the string
"""
# search()
st = "The rain in Spain can't go in vain"
res = re.search("\s", st)
res1 = re.search("Portugal", st)
print(f"The first whitespace character is found at position:{res.start()}")
print(res1) # Here it will return None as there is no match







