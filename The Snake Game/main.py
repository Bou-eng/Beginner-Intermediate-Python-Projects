from turtle import Screen, Turtle
import time
from Snake import Snake
from Food import Food
from Scoreboard import Score
snake = Snake()
food = Food()
screen = Screen()
score = Score()


screen.setup(width=500, height=500)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
game_is_on = True


while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # Detect the collusion with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()
    # Detect the collusion with wall
    if snake.head.xcor() > 244 or snake.head.xcor() < -244 or snake.head.ycor() > 244 or snake.head.ycor() < -244:
        score.reset()
        score.update_scoreboard()
        snake.reset()
    # Detect collusion with tail
    for segment in snake.all_segments[1:-1]:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            score.reset()
            score.update_scoreboard()
            snake.reset()

screen.exitonclick()
