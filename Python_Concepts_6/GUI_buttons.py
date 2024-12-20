"""
buttons:- you click it, then it does stuff
"""
from tkinter import *

count = 0

def click():
    global count
    count += 1
    print(f"You have clicked on button {count} times!")
window = Tk()
photo = PhotoImage(file="icon_button.png")
window.title("Basic GUI")
button = Button(
    window,
    text="Click Here!",
    font=("Comic Sans", 25, "bold"),
    command=click,
    fg="black",
    bg="gold",
    activebackground="gold", #This sets the background colour which displays when we actually click on button
    activeforeground="black", #This sets the font colour which displays when we actually click on button
    state=ACTIVE, #Using this we can also disable a button by simply changing it to DISABLED
    image=photo,
    compound="bottom",  #It can have values as top, bottom, left, right relative to the text

)
button.pack()
window.mainloop()