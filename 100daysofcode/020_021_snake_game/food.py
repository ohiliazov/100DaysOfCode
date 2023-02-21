import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self):
        super().__init__(shape="circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed(0)
        self.refresh()

    def refresh(self):
        x = random.randint(-280, 280)
        x -= x % 20
        y = random.randint(-280, 280)
        y -= y % 20
        self.goto(x, y)
