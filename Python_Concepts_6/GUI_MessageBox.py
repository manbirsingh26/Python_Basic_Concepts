from tkinter import *
from tkinter import messagebox  # importing messagebox library

window = Tk()


def click():
    # messagebox.showinfo(title="This is an info message box", message="You clicked on button")
    # messagebox.showwarning(title="WARNING", message="You have a virus!")
    # messagebox.showerror(title="ERROR", message="Something went wrong!")
    # if messagebox.askokcancel(title="Ask Ok Cancel", message="Do you want to do the thing?"):
    #   print(f"You want to do the thing!")
    # else:
    #   print(f"You don't want to do this thing!")
    # if messagebox.askretrycancel(title="Ask Retry Cancel", message="Do you want to retry the thing?"):
    #   print(f"You want to retry the thing!")
    # else:
    #   print(f"You don't want to retry this thing!")
    # if messagebox.askyesno(title="Ask Yes or NO", message="Do you like cake?"):
    #    print(f"I like it too")
    # else:
    #   print(f"Why you don't like it?")
    # answer = messagebox.askquestion(title="Ask Question", message="Do you like pie?")
    # if answer == "yes":
    #   print(f"I like pie too")
    # else:
    #   print(f"Why you don't like pies?")
    # print(messagebox.askyesnocancel(title="Yes No Cancel", message="Do you like to code?"))
    answer = messagebox.askyesnocancel(title="Yes No Cancel", message="Do you like to code?", icon="error")
    # icon can have values as info, warning, error or question
    if answer == True:
        print(f"You like to code")
    elif answer == False:
        print(f"You do not like to code")
    else:
        print(f"You have no idea")


button = Button(window, command=click, text="click me")
button.pack()

window.mainloop()
