from turtle import Screen
import time
from snack_game import Snack
from food import Food
from score import Score

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("Green")
screen.title("Mobile Snake Game")
screen.tracer(0)

food=Food()
score=Score()
snake=Snack()
screen.listen()
screen.onkey(snake.Down, "Down")
screen.onkey(snake.Up, "Up")
screen.onkey(snake.Left, "Left")
screen.onkey(snake.Right, "Right")

on=True
T=0.1
while on:
    screen.update()
    time.sleep(T)
    snake.move()
    
    #detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase()
        T-=0.0005
        time.sleep(T)
    
    #detect collision with wall
    if snake.head.xcor()>280 or snake.head.ycor()>260:
        on=False 
        score.over()
    elif snake.head.xcor()<=-300 or snake.head.ycor()<=-300:
        on=False 
        score.over()
    
    #detect collision with tail
    for seg in snake.segment:
        if seg==snake.head:
            pass
        elif snake.head.distance(seg)<10:
            on=False 
            score.over()

screen.exitonclick()