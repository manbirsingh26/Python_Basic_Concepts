"""
Print all the vowels present in the provided text(try to print it only once)
"""
a = "The quick brown fox jumps over the lazy dog"
x = len(a)
#res = []
res = set()  # we are using sets so that values don't get repeated
for i in range(0, x):
    if a[i] == "A" or a[i] == "E" or a[i] == "I" or a[i] == "O" or a[i] == "U" or a[i] == "a" or a[i] == "e" or a[i] == "i" or a[i] == "o" or a[i] == "u":
        res.add(a[i])
        #res.append(a[i])
        #res1 = set(res)
#print(res1)
print(res)