import random
from turtle import Turtle

COLORS = ["red", "blue", "green", "yellow", "orange", "purple", "white"]


class Food(Turtle):
    def __init__(self):
        super().__init__(shape="circle")
        self.penup()
        self.speed(0)
        self.refresh()

    def refresh(self):
        radius = random.randint(3, 10) / 10
        self.shapesize(stretch_len=radius, stretch_wid=radius)
        self.color(random.choice(COLORS))
        x = random.randint(-280, 280)
        x -= x % 20
        y = random.randint(-280, 280)
        y -= y % 20
        self.goto(x, y)
