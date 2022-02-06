import turtle as t
import random

tim = t.Turtle()

side_angle = [ 0, 180, 90]
color = ["navy", "green yellow", "gold", "crimson", "orchid"]

game = True
while game:
    angle = random.choice(side_angle)
    tim.forward(20)
    tim.setheading(angle)
    tim.color(random.choice(color))
    tim.width(10)
    if not tim.getscreen():
        game = False

