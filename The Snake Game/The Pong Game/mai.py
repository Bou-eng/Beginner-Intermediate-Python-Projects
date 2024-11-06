from turtle import Turtle, Screen
import random
from paddle import Paddle
from ball import Ball
from scoreboard import Score
import time
# Screen stuff
screen = Screen()
screen.bgcolor("Black")
screen.setup(width=700, height=450)
screen.title("The Pong Game")
screen.tracer(0)

# Paddles stuff
right_paddle = Paddle(x_coordinate=320)
left_paddle = Paddle(x_coordinate=-320)

# Ball stuff
ball = Ball()

# Score class
score = Score()


# Screen stuff Part-2
screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "s")
screen.onkey(left_paddle.go_down, "z")


game_is_on = True
while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    # Detect collusion with the wall
    if ball.ycor() > 210 or ball.ycor() < -210:
        ball.bounce_y()

    # Detect collusion with the right paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 300 or ball.distance(left_paddle) < 50 and ball.xcor() < -300:
        ball.bounce_x()

    # detect if the ball have skept the wall of one of the paddles
    if ball.xcor() > 340:
        ball.reset_ball_position()
        score.left_point()

    if ball.xcor() < -340:
        ball.reset_ball_position()
        score.right_point()

screen.exitonclick()
