from turtle import Turtle

class Score(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score=0
        self.penup()
        with open("High_Score.txt",mode="r") as file:
            self.High_Score=int(file.read())
        file.close()
        self.goto(0,265)
        self.write(f"SCORE : {self.score}  High Score : {self.High_Score}",align="center",font=("Arial",20,"normal"))
        self.hideturtle()
    
    def increase(self):
        self.score+=1
        if(self.score>self.High_Score):
            self.High_Score=self.score
        self.clear()
        self.penup()
        self.goto(0,265)
        self.write(f"SCORE : {self.score}  High Score : {self.High_Score}",align="center",font=("Arial",20,"normal"))
        self.hideturtle()
    
    def over(self):
        self.goto(0,0)
        self.write(f"Game Over",align="center",font=("Arial",22,"normal"))
        with open("High_Score.txt",mode="w") as file:
            file.write(str(self.High_Score))
        file.close()
    
    def get_score(self):
        return self.High_Score
    
    
    
        