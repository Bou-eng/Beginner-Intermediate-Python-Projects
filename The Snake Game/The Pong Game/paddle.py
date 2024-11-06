from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x_coordinate):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=4.9, stretch_len=0.6)
        self.goto(x=x_coordinate, y=0)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(x=self.xcor(), y=new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(x=self.xcor(), y=new_y)
