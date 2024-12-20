from tkinter import *
from tkinter import colorchooser
def click():
    colour = colorchooser.askcolor()
    #print(f"Colour(RGB, Hex Value):-{colour}")
    window.config(bg=colour[1])   #change background colour
    

window = Tk()
window.geometry("420x420")
button = Button(text="Click Me", command=click)
button.pack()
window.mainloop()