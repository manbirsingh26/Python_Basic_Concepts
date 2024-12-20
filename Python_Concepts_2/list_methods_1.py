"""
1.count()
2.append()
3.insert()
4.remove()
5.pop()
6.extend()
7.index()
8.sort()
9.sorted
10.reverse()

"""
lis = list()
#Adding elements using append(): adds at the end and we can also add another list into our list as a whole element
lis.append(20)
lis.append(40)
lis.append(60)
lis.append(25)
lis.append(15)
lis.append(30)
lis.append(45)
lis.append(55)
lis.append(15)
lis.append(70)
print(lis)

#count(): gives no of occurrences of an element in a list
print(lis.count(lis[1]))  #count of second element in the list
print(lis.count(15))  #count of 15 in the list

#sorting
#sort(): directly sorts and returns the original list by default in ascending order(and is case sensitive in case of alphabetical list)
lis.sort()
print(lis)
lis.sort(reverse=True)  #In order to sort in descending order, we change value of reverse to True which by def is False
print(lis)
ais = ["Manbir", "Harleen", "avneet", "Kash", "nabi"]
#ais.sort()  # if we simply sort it, the capital words will be placed first by def as it is case sensitive
#which will generate wrong results, so we modify it
ais.sort(key=str.lower)  # now its case insensitive

print(ais)

#reverse()
lis.reverse()
print(lis)

#remove()
lis.remove(20)  # And we can also use indexing instead of direct value of element
print(lis)

#index(): prints index of first occurrence of an element
print(lis.index(15))


