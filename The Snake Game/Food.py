from turtle import Turtle
import random

colors = ["purple", "red", "white", "blue", "green", "pink", "brown", "aqua"]


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color(random.choice(colors))
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-230, 230)
        random_y = random.randint(-230, 230)
        self.goto(random_x, random_y)



