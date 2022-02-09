import random
from turtle import Turtle, Screen

color = ["green", "red", "blue", "black", "orange", "gray"]
is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="make your bet", prompt="which turtle will win the win? Enter the color: ")
height_ful = [-100, -50, 0, 50, 100]
all_turtles = []

for item in range(0, 5):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=-230, y=height_ful[item])
    new_turtle.color(color[item])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"you win and the winning color is {winning_color}")
            else:
                print(f"you lose and the winning color is {winning_color}")
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()

