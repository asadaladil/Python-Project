from turtle import Turtle


class Ball(Turtle):
    
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len=1.5,stretch_wid=1.5)
        self.color("white")
        self.goto(0,0)
        self.penup()
        self.x=5
        self.y=5
        
    def move(self):
        x=self.xcor()+self.x
        y=self.ycor()+self.y
        self.goto(x,y)
    
    def bounce(self):
        self.y*=-1
        
    def bounce_back(self):
        self.x*=-1
    
    def reset_ball(self):
        self.goto(0,0)
    
    def reset_speed(self):
        return 0.08
        
    