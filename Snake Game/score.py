from turtle import Turtle

class Score(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score=0
        self.penup()
        self.goto(0,265)
        self.write(f"SCORE : {self.score}",align="center",font=("Arial",20,"normal"))
        self.hideturtle()
    
    def increase(self):
        self.score+=1
        self.clear()
        self.penup()
        self.goto(0,265)
        self.write(f"SCORE : {self.score}",align="center",font=("Arial",20,"normal"))
        self.hideturtle()
    
    def over(self):
        self.goto(0,0)
        self.write(f"Game Over",align="center",font=("Arial",22,"normal"))
        