from turtle import Turtle, Screen
from scoreboard import Score
from player import Player
from car_manager import CarManager
import time

screen = Screen()
screen.title("Turtle Crossing Game")
screen.setup(width=600, height=500)
screen.tracer(0)

# Screen things
player_turtle = Player()
car_manager = CarManager()
car_manager.hideturtle()
score = Score()
screen.listen()
screen.onkey(player_turtle.go_up, "Up")

is_game_on = True

while is_game_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_car()

    # Detect the collusion with the cars
    for car in car_manager.all_cars:
        if car.distance(player_turtle) < 20:
            is_game_on = False
            score.game_over()
    # Detect if the turtle reached the other side of the screen
    if player_turtle.ycor() > 240:
        car_manager.level_up()
        player_turtle.goto_start()
        score.score_up()




screen.exitonclick()