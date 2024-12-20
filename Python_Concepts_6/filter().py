"""
filter() : It creates  a collection of elements from an iterable for which a function returns true.
Syntax:-
filter(function,iterable)
"""
# Example
# WAP to check if your friends are of legal driving age or not
friends = [("Abid", 22),
           ("Ashish", 23),
           ("Sushant", 24),
           ("Manik", 20),
           ("Monika", 19),
           ("Joe", 17)]
legal = lambda info: info[1] >= 21
result = list(filter(legal, friends))
print(f"The below buddies can legally drive:-")
for i in result:
    print(i)