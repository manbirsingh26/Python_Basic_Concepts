"""
textwidget:- functions like a text area, we can enter multiples lines of text
"""
from tkinter import *
def submit():
    inputt = text.get("1.0", END)
    print(f"{inputt}")
window = Tk()
text = Text(window,
            bg="sky blue",
            font=("Ink Free", 25),
            height=10,
            width=25,
            padx=20,
            pady=20,
            foreground="red"
            )
text.pack()
button = Button(window, text="submit", command=submit)
button.pack()
window.mainloop()
