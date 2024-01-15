import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=2)
        self.color(COLORS[random.randint(0,5)])
        self.setpos(x=random.randint(-280,280),y=random.randint(-240,240))
        self.move_distance=STARTING_MOVE_DISTANCE

    def move_left(self):
        self.goto(self.xcor()-self.move_distance,self.ycor())

    def speedup(self):
        self.move_distance+=MOVE_INCREMENT