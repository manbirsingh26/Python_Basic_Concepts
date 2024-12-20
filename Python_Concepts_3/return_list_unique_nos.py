"""
Given a list, return a new list containing the unique elements of first list
"""
def unique(A):
    x = set(A)
    print(list(x))
    return 0
a = [1, 2, 3, 4, 1, 2, 4, 5, 9, 0, 1]
unique(a)