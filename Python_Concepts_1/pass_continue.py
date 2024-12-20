# Using while loop
i = 1
while i <= 10:
    if i == 5:
        i += 1
        continue  # it is used to skip a particular iteration
    print(i)
    i += 1
# Using for loop
for i in range(1, 11):
    if i == 5:
        continue
    print(i)

# pass statement
# it is used to avoid an error when empty code is not allowed as nothing happens when it's executed
# so it is basically the placeholder for future code
for x in [0, 1, 2]:
    pass


def myfunction():
    pass
