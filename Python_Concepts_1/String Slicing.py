# : is used to do string slicing on order to access substrings from a string
# syntax is [start:end]
# also it can be [start:end:jump]
s = "Manbir Singh"
print(s[0:])  # all characters
print(s[0:4])  # from 1st to 4rd
print(s[2:])  # from 3rd to last
print(s[:3])  # first three characters
print(s[-5:])  # last five characters
print(s[-1:])  # last character(h)
print(s[-1::-1])  # also all in reverse
print(s[:-1])  # all characters except last
print(s[::-1])  # all in reverse
print(s[(len(s)-1)::-1])  # also all in reverse(len(str) -1 is used to find last index of a string
print(s[0:6:2])  # will print Mni
print(s[-12:])  # this will also print all characters
