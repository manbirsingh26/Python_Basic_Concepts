f = open("demo_file.txt", "a")
f.write("Python is a fun to learn language.\n")
f.write("I love learning it.\n")
f.close()
f = open("demo_file.txt", "r")
print(f.read())
