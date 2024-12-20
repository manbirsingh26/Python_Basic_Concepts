from tkinter import *
from tkinter import filedialog

def saveFile():
    file = filedialog.asksaveasfile(initialdir="C:\\Users\\LENOVO\\PycharmProjects\\Python_Concepts_Part6",
                                    defaultextension=".txt",
                                    filetypes=[
                                        ("Text file", ".txt"),
                                        ("HTML file", ".html"),
                                        ("All files", ".*")
                                    ])
    if file is None:
        return
    filetext = str(text.get(1.0, END))
    #fileletext = input("Enter some text I guess: ") #Use this if you want to use console
    file.write(filetext)
    file.close()

window = Tk()
button = Button(text="save", command=saveFile)
button.pack()
text = Text(window)
text.pack()
window.mainloop()