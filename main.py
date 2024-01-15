import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title("Turtle Crossing")
screen.setup(width=600, height=600)
screen.tracer(0)
cars=[]
flag=0

player=Player()
for i in range(0,20):
    car_manager=CarManager()
    cars.append(car_manager)

score=Scoreboard()

screen.listen()
screen.onkey(player.move_up,"w")

game_is_on = True
while game_is_on:

    if player.ycor()>280:
        score.update_level()
        player.reset_pos()
        flag=1
    score.write_level()
    for car in cars:
        if ((player.ycor()+15)>=(car.ycor()-10) and (player.ycor()+15)<=(car.ycor()+10) or (player.ycor()-10)>=(car.ycor()-10) and (player.ycor()-10)<=(car.ycor()+10))  and player.distance(car)<25:
            game_is_on=False
            score.gameover()
    for car in cars:
        if flag==1:
            car.speedup()

        car.move_left()
        if car.xcor()<-280:
            car.setpos(x=280,y=random.randint(-280,280))
    time.sleep(0.1)
    screen.update()
    flag=0


screen.exitonclick()