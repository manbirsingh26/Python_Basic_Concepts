"""
Sets support some methods which are:-
1. add()- for adding single element
2. update(iterable(lists,tuples,dictionaries,set))
3. pop()- removes any random element, not sure what it is
4. remove(particular element)
5. intersection()- same as maths intersection
6. union()- same as maths union
7. symmetric-difference()
8. difference()
9. issubset()
"""
veggies = {"cucumber", "radish", "carrot", "spinach", "knolkhol"}
print(veggies)
veggies.add("pumpkin")  #add() method
print(veggies)
veggies_1 = {"bottle_gourd", "bitter_gourd"}
veggies.update(veggies_1)  #update() method
print(veggies)
veggies.update({"kiwi", "mango"})
fruits = ["apple", "banana", "dragonfruit"]
veggies.update(fruits)
print(veggies)
#veggies.pop()  #pop() method usage
veggies.remove("dragonfruit")   #remove method usage
print(veggies)
a = {1, 2, 3, 4, 5, 6, 1, 2, 5}
b = {1, 5, 3, 12, 13, 15}
c = {12, 13, 15}
x = a.intersection(b)  #Only common values of both will be sored in mew set
print(x)
d = a.union(b)   #All the non-repeatable values of both sets will be there in new set
print(d)
e = a.symmetric_difference(b)   #All the elements which are not there in both sets(non-common values)
print(e)
f = a.difference(b)   #Keeps the items from first set which are not present in other set
print(f)
print(c.issubset(b))
print(c.issubset(a))

