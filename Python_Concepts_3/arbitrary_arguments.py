"""
Arbitrary Arguments
Syntax:
*args
"""
def func(*args):
    #print(type(args)) #This will return tuple
    for i in args:
        print(i**2 if str(i).isnumeric() else i, end=" ")
    return 0
func(1, 2, 3, 4, 5, "Manbir", "Harleen", 6)
print()
func("A", "B", "C", "D", "E", 15)


