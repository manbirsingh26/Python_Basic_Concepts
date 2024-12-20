#sorted(): it sorts and returns the copy of original list
x = [10, 15, 20, 5, 12, 25, 21]
x1 = sorted(x)
print(f"Original list is: {x}")  #Original list will be unchanged
print(f"Sorted list is: {x1}")

#pop(): deletes and returns the last element of the list
print(x.pop())
print(x.pop(1))  # We can also mention index of element which we want to delete)

#insert(): adds the element at a given index
x.insert(2, 50)  #list.insert(index, value)
print(x)

# extend(): used to merge lists with lists and strings
x1 = ["a", "b", "c", "d"]
x2 = "Rahul"
x.extend(x1)
print(x)
x.extend(x2)
print(x)