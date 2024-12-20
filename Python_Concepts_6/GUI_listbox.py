"""
listbox:- listing of selectable text items within it's own container
"""
from tkinter import *

def submit():
    food = []
    for index in listbox.curselection():
        food.insert(index, listbox.get(index))
    print(f"You have ordered the following item(s):-")
    for index in food:
        print(f"{index}")

    #print(f"You have ordered {listbox.get(listbox.curselection())}")

def add():
    listbox.insert(listbox.size(), entrybox.get())
    listbox.config(height=listbox.size())

def delete():
    for index in reversed(listbox.curselection()):
        listbox.delete(index)

    listbox.config(height=listbox.size())

window = Tk()

listbox = Listbox(window,
                  bg="#ECDC0E",
                  font=("Constantia", 40),
                  width=12,
                  selectmode=MULTIPLE)
listbox.pack()

listbox.insert(1, "Pizza")
listbox.insert(2, "Hamburger")
listbox.insert(3, "Momo")
listbox.insert(4, "Noodles")
listbox.insert(5, "Hotdog")
listbox.insert(6, "Salad")


listbox.config(height=listbox.size())

#entrybox = Entry(window)
#entrybox.pack()

submitbutton = Button(window,
                      text="Submit",
                      command=submit)
submitbutton.pack()

entrybox = Entry(window)
entrybox.pack()

addbutton = Button(window,
                   text="Add Item",
                   command=add)
addbutton.pack()

deletebutton = Button(window,
                      text="Delete Item",
                      command=delete)
deletebutton.pack()

window.mainloop()
