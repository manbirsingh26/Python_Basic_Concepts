from tkinter import *
from tkinter import filedialog


def openfile():
    filepath = filedialog.askopenfilename(initialdir="C:\\Users\\LENOVO\\PycharmProjects\\Python_Concepts_Part6",
                                          title="Open File Okay?",
                                          filetypes=(("text files", "*.txt"),
                                                     ("all files", "*.*"))

                                          )
    file = open(filepath, "r")
    print(file.read())
    file.close()


window = Tk()
button = Button(text="Open", command=openfile)
button.pack()
window.mainloop()
