a = [1, 2, 3]
b = ("audi", "toyota", "cadillac")
c = ("germany", "japan", "u.s.a")
res = (a, b, c)
print(res)
# We also can't change any element in 2D-Tuple as it is unchangeable
# But we can do changing inside that element which is a list e.g here "a" is a list
res[0][0] = 1935
res[0][1] = 1955
res[0][2] = 1940
print(res)
print("Taking 2D tuple as input manually from user...")
r = int(input("Enter the size (number of rows) of tuple:-"))
tup = [tuple(input().split()) for _ in range(r)]  #As we are using list comprehension, we need to convert result into
print(tuple(tup))  # to convert list into tuple