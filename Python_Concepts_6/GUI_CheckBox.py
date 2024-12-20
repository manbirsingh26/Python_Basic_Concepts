from tkinter import *
window = Tk()
window.title("Basic GUI")

x = IntVar()
#x = BooleanVar()  #Similarly we can also use StringVar(), then we change onvalue and offvalue to strings
img = PhotoImage(file="PY_LOGO.png")

def display():
    #if x.get():
    if x.get() == 1:
        print(f"You agree to terms and conditions!")
    else:
        print(f"You don't agree with terms and conditions!")


check_button = Checkbutton(window,
                           text="Agree to Terms and Conditions",
                           variable=x,
                           onvalue=1,
                           #onvalue=True,
                           offvalue=0,
                           #offvalue=False,
                           command=display,
                           font=("Comic Sans", 30, "bold"),
                           fg="red",
                           bg="black",
                           activeforeground="red",
                           activebackground="black",
                           padx=25,
                           pady=15,
                           image=img,
                           compound="left"
                           )
check_button.pack()
window.mainloop()