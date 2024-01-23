from tkinter import *

window=Tk()
window.title("Feet to Inch Converter")
window.minsize(width=500,height=400)

lb=Label(text="Enter the value of Feet",font=("Times New Roman",20,"bold"))
lb.pack()

ip=Entry()
ip.pack()
def calculate():
    x=float(ip.get())*12
    lb1.config(text=f"The Value in inches is {x}")
bt=Button(text="Submit",font=("Times New Roamn",15,"bold"),command=calculate)
bt.pack()

lb1=Label(text="Empty Input",font=("Times New Roman",20,"bold"))
lb1.pack()
window.mainloop()