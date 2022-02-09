from turtle import Turtle, Screen

screen = Screen()
screen.bgcolor("black")
screen.setup(height=600, width=600)
screen.title("snake game")
starting_position = [(0, 0), (-20, 0), (-40, 0)]
for position in starting_position:
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.goto(position)
screen.exitonclick()
