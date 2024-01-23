import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing Capstone")
screen.tracer(0)

player=Player()
car=CarManager()
score=Scoreboard()


screen.listen()
screen.onkey(player.go_up,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    car.create_car()
    car.move_car()
    
    # detect collision
    for cr in car.all_car:
        if cr.distance(player)<30:
            score.game_over()
            game_is_on=False
    
    #checking crossing
    if player.at_the_finish_line():
        player.go_to_start()
        score.level_up()
        car.speed_up()


screen.exitonclick()
