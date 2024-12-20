"""
GUI(Graphical User Interface)
widgets:- GUI elements like buttons, textboxes, labels, images, etc
windows:- serves as a container to hold or contain these widgets
"""
from tkinter import *

window = Tk() #This instantiate an instance of a window
window.geometry("420x420") #This geometry function helps us to change size of our window
window.title("Manbir Singh First GUI Prog") #Changing the title of windows
#Changing the icon of our Windows
icon = PhotoImage(file="coffee-cartoon.png")
window.iconphoto(True, icon)
#window.config(background="crimson") #Changing the background colour of the windows
window.config(background="#4095c9") #Can also use hex value of colours

window.mainloop()  #This  displays window on computer screen and also listen for events
