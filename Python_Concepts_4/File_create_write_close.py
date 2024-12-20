#f = open("demo_file_2.txt", "x")  #This is useful if just want to create an empty file.
f = open("demo_file2.txt", "w")  #This automatically creates the new file if it doesn't exist.
f.write("This is the second demo file.\n"
        "This is also for testing purposes.")
f.close()
# If we write to a file which already exists then it overrides the existing content of file.