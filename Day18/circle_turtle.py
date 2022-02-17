import random
import turtle as t


color = ["navy", "green yellow", "gold", "crimson", "orchid"]
tim = t.Turtle()
game = True
while game:
    tim.circle(50)
    tim.speed(50)
    tim.color(random.choice(color))
    tim.setheading(tim.heading() + 10)

