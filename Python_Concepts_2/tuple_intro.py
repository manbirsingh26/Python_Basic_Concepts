"""
Tuples are:
1.ordered collection of data(supports indexing)
2.Unchangeable(Need to convert to list to change and then convert list back to tuple)
3.Can contain multiple types of data
4.Iterable
"""
#Creating a tuple
fruits = ("apple", "banana", "dragonfruit", "cherry", "kiwi")
names = tuple()
x = tuple("manbir")  # Another Method to create tuple-tuple(iterable)
print(x)
print(fruits)
print(fruits[2])  #Using indexing
a = (1, 2, 3, 4, 5)
print(a[::-1])  # Also supports slicing
print()
#names = tuple(map(int, input().split()))  #This only way to add elements in empty tuple as there's no built method
#but the above approach only takes one type of input, inorder that it takes mul types, we can modify it
#we can use comprehension
raw_input = input("Enter elements of tuple:-").split()
names = tuple(int(i) if i.isdigit() else i for i in raw_input)
print(names)
#Iterating
for i in range(0, len(names)):
    print(names[i])

# But we can covert it into a list() to add elements using append() and can also do other modifications
brands = ("audi", "bmw", "mercedes-amg", "porsche", "lamborghini")
bran1 = list(brands)
bran1.append("toyota")
bran1.append("hyundai")
bran1.append("kia")
bran1.remove(bran1[3])
bran1.insert(1, "ferrari")
#bran1.sort(key=str.lower)
bran2 = tuple(bran1)
print(bran2)  # Finally converting back into tuple after doing operations


