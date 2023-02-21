from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_pos: int, y_pos: int):
        super().__init__("square")
        self.penup()
        self.setheading(90)
        self.color("white")
        self.goto(x_pos, y_pos)
        self.shapesize(stretch_wid=1, stretch_len=5)

    def go_up(self):
        if self.ycor() < 250:
            self.forward(20)

    def go_down(self):
        if self.ycor() > -250:
            self.backward(20)
