from tkinter import *

def submit():
    print(f"The temperature is: {scale.get()} degrees C")

window = Tk()
hot = PhotoImage(file="fire.png")
hotlabel = Label(image=hot)
hotlabel.pack()
scale = Scale(window,
              from_=100,
              to=0,
              length=600,
              orient=VERTICAL,  #Can also be horizontal
              font=('Consolas', 20),
              tickinterval_=10,  #This shows indicators on scale
              #showvalue_=0, #hides current value
              resolution_=5, #increment of slider
              troughcolor_="#69EAFF",
              fg_="#FF1C00",
              bg_="black",

              )
scale.set(0)  #sets current default value of slider, we can use any value
scale.pack()
cold = PhotoImage(file="Cold_Emoji.png")
coldlabel = Label(image=cold)
coldlabel.pack()
button = Button(window, text="submit", command=submit)
button.pack()

window = mainloop()