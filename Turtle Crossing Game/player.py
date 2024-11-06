from turtle import Turtle
MOVE_DISTANCE = 10


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("black")
        self.left(90)
        self.goto(x=0, y=-220)

    def goto_start(self):
        self.goto(x=0, y=-220)

    def go_up(self):
        self.forward(MOVE_DISTANCE)
