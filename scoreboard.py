from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level=1
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(x=-240,y=270)
        self.write_level()

    def write_level(self):
        self.clear()
        self.write(f"LEVEL:{self.level}", align="center", font=FONT)

    def update_level(self):
        self.level+=1
    def gameover(self):
        self.goto(0,0)
        self.write("GAME OVER!!!", align="center", font=FONT)