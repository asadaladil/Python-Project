from turtle import Turtle,Screen
import pandas
screen=Screen()
screen.title("USA States Map")
image="blank_states_img.gif"
screen.addshape(image)

tur=Turtle()
tur.shape(image)
data=pandas.read_csv("50_states_USA.csv")
states=data["state"].tolist()
on=True
a=0
while on:
    answer=screen.textinput(title="Write the name of States",prompt=f"Guess the States {a}/50").title()
    if answer in states:
        T=Turtle()
        T.hideturtle()
        T.penup()
        data_cor=data[data["state"]==answer]
        T.goto(int(data_cor.x),int(data_cor.y))
        T.write(answer)
        states.remove(answer)
        a+=1
    if a==50 or answer=="Exit":
        on=False
    
print("Missing States: ")
for i in states:
    print(i)
