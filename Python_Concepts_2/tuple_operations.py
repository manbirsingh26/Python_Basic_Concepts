"""
It only supports following operations:-
1. count()
2. index()
3. concatenation(+) of two tuples
4. unpacking a tuple

"""
fruits = ("apple", "banana", "mango", "kiwi", "strawberry", "apple", "dragonfruit", "cherry", "peach", "orange")
print(fruits.count("apple"))   #count
print(fruits.index("cherry"))  #index
#Iterating
for i in range(0, len(fruits)):
    print(fruits[i])
# Concatenation
a = (1, 2, 3, 4, 5)
b = ("a", "b", "c", "d", "e")
joint = a + b
print(joint)

# Unpacking a tuple
a, b, c = 1, 2, 3   #This is same as a = 1 and b =2 and this concept is called unpacking
#print(a, b, c)

#Example 1
# Extracting values  back into variables(no of variables must the no of values)
d, e, f, g, h, i, j, k, l, m = fruits
print(d, e, f, g, h, i, j, k, l, m, sep=",")
# If no of variables are not matching values then we can add asterisk(*) to variable name to
# take remaining values as list.
x, y, z, c, n, *o = fruits
print(x, y, z, c, n, o, sep=",")
# We can also add * to the name of variable other than the last variable
x1, y1, z1, *c1, n1, o1, b1 = fruits
print(x1, y1, z1, c1, n1, o1, b1, sep=",")




