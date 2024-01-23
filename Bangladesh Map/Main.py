from turtle import Turtle,Screen
import pandas

image="Bangladesh_districts.gif"

screen=Screen()
screen.title("Guess the District Name of Bangladesh")
screen.addshape(image)
screen.setup(width=800,height=850)

tur=Turtle()
tur.shape(image)
tur.penup()

data=pandas.read_csv("District_Co_ordinate.csv")
district=data["District"].tolist()
b=len(district)
on=True
a=0
while on:
    answer=screen.textinput(title="Write the name of District",prompt=f"Guess the District {a}/64").title()
    if answer in district:
        T=Turtle()
        T.hideturtle()
        T.penup()
        data_cor=data[data["District"]==answer]
        T.goto(int(data_cor.x),int(data_cor.y))
        T.write(answer,font=("Times New Roman",10,"bold"))
        district.remove(answer)
        a+=1
    if a==b or answer=="Exit":
        on=False

print("missing district")
for i in district:
    print(i)