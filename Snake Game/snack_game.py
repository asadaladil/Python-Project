from turtle import Turtle
U=90
D=270
L=180
R=0

class Snack:
    segment=[]
    head=[]
    def __init__(self) -> None:
        self.starting_position=[(0,0),(-20,0),(-40,0)]
        self.segment=[]
        self.create_snack()
    
    def create_snack(self):
        for i in self.starting_position:
            self.add_Seg(i)
        self.head=self.segment[0]
    
    def add_Seg(self,pos):
        new_Seg=Turtle("square")
        new_Seg.penup() # straight line will be removed
        new_Seg.goto(pos)
        self.segment.append(new_Seg)
    
    def extend(self):
        self.add_Seg(self.segment[-1].position())
    
    def move(self):
        for i in range(len(self.segment)-1,0,-1):
            x=self.segment[i-1].xcor()
            y=self.segment[i-1].ycor()
            self.segment[i].goto(x,y)
        self.head.forward(20)
    
    
    def Up(self):
        if self.head.heading() != D:
            self.head.setheading(90)
    
    def Down(self):
        if self.head.heading() != U:
            self.head.setheading(-90)
        
    def Right(self):
        if self.head.heading() != L:
            self.head.setheading(0)
        
    def Left(self):
        if self.head.heading() != R:
            self.head.setheading(180)
    
    
    
