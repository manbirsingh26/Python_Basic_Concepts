"""
Sets are data structures which are:=
1. Unordered
2. Unindexed(Indexing is not supported)
3. Contain Unique Values(Does not supports duplicate values)
4. Mutable(New Values can be added,Existing values can only be removed but cannot be changed )
5. Iterable
"""
#Creating a set
a = {}  #This is correct but if we check type, it will show type as dict
a = set()
#Another Method is:-
#set_name = set(iterable(lists,set,tuple,etc.))
b = [1, 2, 3, 4, 5, 6, 2, 3, 7]
a = set(b)
print(a)   #Here only unique values will be shown, repeated will not like in list b
c = {"a", "b", "c", "d", "e", "a", "c"}
print(c)   #Here also only unique values will be shown,repeated will not be
d = set("manbirsingh")  #Here it will form a set where elements will be all the unique characters of string
print(d)
# Iteration
for i in d:
    print(i)


