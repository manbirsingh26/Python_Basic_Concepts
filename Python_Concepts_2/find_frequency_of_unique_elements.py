"""
Given a tuple (or a list) find the frequency of unique elements and print the following:-
>> unique_element: frequency
"""
tup = ("manbir", "harleen", "manbir", "harleen", "avneet", ["a", "b", "c"], [1, 2, 3], ["a", "b", "c"])
# Method 1
freq = {}
for i in tup:
    if isinstance(i, list):  #We convert list elements to tuples because list elements can't be used as dict keys
        i = tuple(i)   #Only hashable types like tuples can be used as dict keys
    freq[i] = tup.count(i)
for key, value in freq.items():
    print(f"{key}:{value}")

#Method 2
"""
tup = ("manbir", "harleen", "manbir", "harleen", "avneet", ["a", "b", "c"], [1, 2, 3], ["a", "b", "c"])
freq = {}

for i in tup:
    if isinstance(i, list):  
        i = tuple(i)   
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1
for key, value in freq.items():
    print(f"{key}:{value}")
    """

