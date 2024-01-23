from tkinter import *
import time


window=Tk()
window.title("My First Tkinter Project")
window.minsize(width=500,height=300)

my_label=Label(text="Welcome to my show")
my_label.pack()


def button_click():
    new_text=input_.get()
    my_label.config(text=new_text)


input_=Entry()
input_.pack()
button=Button(text="Click Me",command=button_click)
button.pack()

window.mainloop()