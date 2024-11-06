import turtle
from turtle import Turtle, Screen
import random
is_race_on = False
screen = Screen()
screen.title("The Turtle Race")
winning = Turtle()
winning.hideturtle()
FONT = ("Courier", 15, "normal")
screen.setup(500, 400)
user_choice = screen.textinput(title="Make your choice", prompt="Which turtle do you think will win the race? : \n"
                                                                "Blue\nBlack\nRed\nGreen\nYellow\nPurple")
colors = ["blue", "black", "red", "green", "yellow", "purple"]
all_turtles = []
y_positions = [-70, -40, -10, 20, 50, 80]
for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.speed("fastest")
    new_turtle.goto(x=-230, y=y_positions[i])
    all_turtles.append(new_turtle)

if user_choice:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.color()
            if winning_color == user_choice:
                print(f"You got it right :) The {winning_color} turtle won the race")
                winning.write("You got it right :)", align="center", font=FONT)
            else:
                print(f"You didn't get it right :( The {winning_color} turtle won the race")
                winning.write("You didn't get it right :)", align="center", font=FONT)
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()




