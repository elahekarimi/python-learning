from turtle import Turtle, Screen

# color = ["green", "red", "blue", "black", "orange", "gray"]

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="make your bet", prompt="which turtle will win the win? Enter the color: ")
tim = Turtle(shape="turtle")
tim.penup()
tim.goto(x=-230, y=-100)
tim.color("red")

deny = Turtle(shape="turtle")
deny.penup()
deny.goto(x=-230, y=-50)
deny.color("orange")

tommy = Turtle(shape="turtle")
tommy.penup()
tommy.goto(x=-230, y=0)
tommy.color("gray")

dony = Turtle(shape="turtle")
dony.penup()
dony.goto(x=-230, y=50)
dony.color("black")

jerry = Turtle(shape="turtle")
jerry.penup()
jerry.goto(x=-230, y=100)
jerry.color("blue")


screen.exitonclick()

