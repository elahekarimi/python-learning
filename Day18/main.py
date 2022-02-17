import turtle as t
import random

tim = t.Turtle()
color = ["navy", "green yellow", "gold", "crimson", "orchid"]


def each(angle_side):
    for _ in range(angle_side):
        angle = 360 / angle_side
        tim.forward(100)
        tim.right(angle)


for shape_side in range(3, 10):
    tim.color(random.choice(color))
    each(shape_side)
