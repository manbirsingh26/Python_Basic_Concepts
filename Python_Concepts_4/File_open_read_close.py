f = open("demo_file.txt", "rt")
print(f.read()) #This will read and display the whole file
#print(f.read(4)) #This also returns the specified no of characters
#print(f.readline()) #This method returns a whole line
#print(f.readline()) #This will return 2nd line as we are using it second time
#print(f.readlines()) #This will print the the whole file line by line
#for x in f:
    #print(x)
# With help of for loop also, we can read the whole file line by line
f.close()