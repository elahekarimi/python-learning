from turtle import Turtle, Screen
import time
import turtle
from snake import Snake


screen = Screen()
turtle.tracer(0)
screen.bgcolor("black")
screen.setup(height=600, width=600)
screen.title("snake game")
snake = Snake()

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

screen.exitonclick()
