import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S state game")
image = "us_photo.gif"
screen.addshape(image)
turtle.shape(image)

guess_state = []
while len(guess_state) < 50:
    answer_state = screen.textinput(title=f"{len(guess_state)} : Guess the State", prompt="What is another state's name: ").title()

    data = pandas.read_csv("50_state.csv")
    all_state = data.state.to_list()
    find_row = data[data.state == answer_state]

    if answer_state in all_state:
        guess_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(int(find_row.x), int(find_row.y))
        t.write(answer_state)


screen.exitonclick()
