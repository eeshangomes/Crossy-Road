from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.left(90)
        self.reset_pos()

    def move_up(self):
        self.goto(self.xcor(),self.ycor()+MOVE_DISTANCE)

    def reset_pos(self):
        self.setpos(STARTING_POSITION)
