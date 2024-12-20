f = open("lamborghini_revuelto_4k.jpg", "rb")
#f.read() #This line will print all the binary data inside the image ans not the image.
d = f.read()
n = open("lamborghini.jpg", "wb")  #This will create new binary file(image) with the entered name.
n.write(d)  #Here we are writing the data to image

