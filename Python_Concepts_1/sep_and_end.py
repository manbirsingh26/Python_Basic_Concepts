print("Manbir", "Harleen", 22, 23, 2002, 2000)
print("Changing the default separation for mul outputs in a single line which is space")
print("Manbir", "Harleen", 22, 23, 2002, 2000, sep=",")
print("Manbir", "Harleen", 22, 23, 2002, 2000, sep="_")
print("Manbir", "Harleen", 22, 23, 2002, 2000, sep="\n")

print("Manbir", 1)
print("Harleen", 2)
print("Lenovo", 3)
print("Changing the default structure for multiple line outputs which is newline")
print("Manbir", 1, end=" $ ")  # We can use anything as a separator
print("Harleen", 2, end=" ")
print("Lenovo", 3, end=" ")
print("Using both together")
print("Manbir", 1, sep="\n", end=" -> ")  # sep works first if both used together
print("Harleen", 2)
