l1 = [1, 2, 3]
l2 = [10, 20, 30]
l3 = [20, 40, 60]
l = [l1, l2, l3]
print(l)  # Individual Lists are added as single elements
# Indexing Style (2-Dimensional)
print("Accessing the elements")
print(l[0])
print(l[0][0])
print(l[0][1])
print(l[0][2])
print(l[1])
print(l[1][0])
print(l[1][1])
print(l[1][2])
print(l[2])
print(l[2][0])
print(l[2][1])
print(l[2][2])
# Iterating 2-D lists
print("Iterating them..")
for i in range(0, len(l)):
    for j in range(0, len(l[i])):
        print(l[i][j], end=" ")
print()
print("Manually taking 2-D lists as input from user..")
s = int(input("Enter the size of the 2-D list:-"))
lis = [list(map(int, input().split())) for _ in range(s)]
print(lis)

