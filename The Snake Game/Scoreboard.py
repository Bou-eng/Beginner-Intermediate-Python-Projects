from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        with open("my_data.txt") as data:
            self.highest_score = int(data.read())
        self.color("white")
        self.goto(x=0, y=220)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.goto(x=0, y=220)
        self.write(f"Score : {self.score} Highest Score : {self.highest_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open("my_data.txt", mode="w") as data:
                data.write(f"{self.highest_score}")
        self.score = 0

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
