from turtle import Turtle
FONT = ("Courier", 16, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 220)
        self.write(f"Level : {self.level} ", align="left", font=FONT)

    def score_up(self):
        self.clear()
        self.level += 1
        self.write(f"Level : {self.level} ", align="left", font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"Game Over :(", align="Center", font=FONT)