"""
label:- an area widget that holds the text and/or image within a window
"""
from tkinter import *

window = Tk()
window.config(bg="crimson")
#Creating label
# fg- font colour
# bg- background colour
# bd- border width
# relief- border style
# padx - padding between text and border from right and left
# pady - padding between text and border from above and below
#photo = PhotoImage(file="C:\\Users\\LENOVO\\Pictures\\Coder.png")
window.title("Manbir GUI")
photo = PhotoImage(file="Coder.png")
label = Label(window,
              text="Do you guys even code?",
              font=("Arial", 40, "bold"),
              fg="#2df505",
              bg="black",
              relief=RAISED, #It can have values as flat, groove, raised, ridge, solid, or sunken
              bd=10,
              padx=25,
              pady=25,
              image=photo,
              compound="bottom", #It can have values as top, bottom, left, right relative to the text
              )
#Adding it to the window
label.pack() #Method 1
#label.place(x=0, y=0)  #Method2

window.mainloop()