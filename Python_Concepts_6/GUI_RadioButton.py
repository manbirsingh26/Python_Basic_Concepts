"""
radio button:- similar to checkbox but we can list a group here and then we can select one from that group
"""
from tkinter import *
food = ["Pizza", "Hamburger", "HotDog"]

def order():
    if x.get() == 0:
        print(f"You have ordered a pizza!")
    elif x.get() == 1:
        print(f"You have ordered a hamburger!")
    elif x.get() == 2:
        print(f"You have ordered a hot dog!")
    else:
        print(f"Huh?")
window = Tk()

pizza_img = PhotoImage(file="pizza_image.png")
ham_img = PhotoImage(file="Hamburger.png")
hotdog_img = PhotoImage(file="Hotdog.png")
foodImages = [pizza_img, ham_img, hotdog_img]

x = IntVar()
for i in range(len(food)):
    radio_button = Radiobutton(window,
                               text=food[i],  #Adds text to radiobuttons
                               variable=x,  #Groups radiobuttons together if they share the same variable
                               value=i,  #Assigns each radiobutton a different value
                               padx=25,
                               font=("Impact", 50),
                               image=foodImages[i], #This adds image to radiobutton
                               compound="left",  #Adds image and text
                               indicatoron=0,  #elimninate circle indicators
                               width=600,  #sets width of radiobuttons
                               command=order
                               )
    radio_button.config()
    radio_button.pack(anchor=W) #This makes radiobuttons all lined up.
window.mainloop()