"""
map(): It applies function to each item in an iterable(list,tuple,etc.)
It is popularly used to take list, tuple, set as input manually
Syntax:-
map(function, iterable)
"""
#Example
# WAP to calculate and display gst on items
items = [
    ("Voltas WindowAC", 22000),
    ("Honda cbr1000", 750000),
    ("Samsung SplitAC", 45000),
    ("Yamaha Xerox155", 130000)
    ]
gst = lambda i: (i[0], round(i[1]*0.28))
result = list(map(gst, items))
print(f"GST on all items is as below:-")
for j in result:
    print(j)
# It is popularly used to take list, tuple, set as input manually.

