from turtle import Screen
from Paddle import Paddle
from Ball import Ball
from score import Score
import time

screen=Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Pong Game")
screen.tracer(0)

l_paddle=Paddle(-380,0)
r_paddle=Paddle(375,0)

ball=Ball()
score=Score()

screen.listen()
screen.onkey(l_paddle.go_up,"Up")
screen.onkey(l_paddle.go_down,"Down")
screen.onkey(r_paddle.go_down,"w")
screen.onkey(r_paddle.go_up,"a")


on=True
hit_l=True
hit_r=True
T=0.08
while on:
    time.sleep(T)
    screen.update()
    ball.move()
    
    #detect collsion with wall
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce()
        
    #detect collision with paddle
    if ball.distance(r_paddle)<50 and ball.xcor()>340 and hit_r:
        hit_r=False
        hit_l=True
        T/=1.2
        ball.bounce_back()
    
    if ball.distance(l_paddle)<50 and ball.xcor()<-340 and hit_l:
        hit_l=False
        hit_r=True
        T/=1.2
        ball.bounce_back()
    
    # paddle misses detect
    if ball.xcor()>380:
        ball.reset_ball()
        score.l_increase()
        T=ball.reset_speed()
        
    
    if ball.xcor()<-380:
        ball.reset_ball()
        score.r_increase()
        T=ball.reset_speed()
        
        
        
screen.exitonclick()

