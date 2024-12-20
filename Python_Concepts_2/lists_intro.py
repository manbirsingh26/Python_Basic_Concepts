"""
Lists are:-
 1.ordered collection of data(Supports indexing)
 2.lists are changeable(mutable)
 3.can contain multiple types of data
 4.lists are iterable
"""
# Creating a list
# Both below methods are correct
#l1 = []
#l2 = list()
#Another Method
l3 = list(i for i in range(0, 4))
l4 = list("manbir")
#print(l3)
#print(l4)
# Simply adding data(of multiple types)
l1 = [10, 20, 30, 40, 50, "X"]
l2 = ["A", "B", "C", "D", "E", 60]
print(f"Initial Lists")
print(l1)
print(l2)


# Changing data(by using indexing)
l1[-1] = "M"
l2[4] = "Z"
print(f"After changing data..")
print(l1)
print(l2)

# Iterating them
print(f"Iterating them..")
for i in range(0, len(l1)):
    print(l1[i])
print(" ")
for i in range(0, len(l2)):
    print(l2[i])

# List_Slicing(same as strings)
print(l1[0:4])  #first 4 elements
print(l1[::])  #whole list
print(l1[::-1])  #reverse of list
print(l1[-1:-4:-1])  #last three elements in reverse

#Taking list as input from user
raw_input = input().split()
l3 = list(int(i) if i.isdigit() else i for i in raw_input)
print(l3)





