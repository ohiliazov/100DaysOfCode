import random
from turtle import Screen, Turtle, colormode

import colorgram

colormode(255)

colors = colorgram.extract("hurst-spot-painting.webp", 31)[1:]


def random_color():
    chosen_color = random.choice(colors).rgb
    return chosen_color.r, chosen_color.g, chosen_color.b


t = Turtle()
t.hideturtle()
t.penup()
t.speed("fastest")

t.setx(-250)
t.sety(-250)

for _ in range(10):
    for _ in range(10):
        t.dot(20, random_color())
        t.forward(50)
    t.setheading(90)
    t.forward(50)
    t.setheading(0)
    t.back(500)

screen = Screen()
screen.exitonclick()
