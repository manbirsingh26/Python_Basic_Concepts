"""
entry widget:- textbox that accepts a single line of user input
"""
from tkinter import *
window = Tk()
window.title("Basic GUI")

entry = Entry(window,
              font=("Arial", 40, "bold"),
              fg="crimson",
              bg="black",
              )
#entry.insert(0, "Enter your name")  #This helps us to insert default text
#entry.config(show="$")  #Using this, only a certain character is shown for all the characters entered e.g password
entry.pack(side=LEFT)

def submit():
    username = entry.get()
    print(f"Hello {username}")
    #entry.config(state=DISABLED)   #This will disable the entry box after the user submits something.
submit = Button(window,
                text="submit",
                command=submit)
submit.pack(side=RIGHT)

def delete():
    entry.delete(0, END)
delete = Button(window,
                text="delete",
                command=delete)
delete.pack(side=RIGHT)

def backspace():
    entry.delete(len(entry.get())-1, END)

backspace = Button(window,
                   text="backspace",
                   command=backspace)
backspace.pack(side=RIGHT)

window.mainloop()