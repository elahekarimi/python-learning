import turtle as t
import random
t.colormode(255)

color = [(202, 164, 189), (238, 240, 245), (150, 75, 49), (223, 201,135), (52, 93, 124)]
tim = t.Turtle()
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
color_range = 100

for dot_count in range(1, color_range+1):
    tim.dot(20, random.choice(color))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)





