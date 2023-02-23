from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__("turtle")
        self.speed(0)
        self.penup()
        self.color("black")
        self.setheading(90)
        self.move_to_start()

    def move_to_start(self):
        self.goto(*STARTING_POSITION)

    def move_forward(self):
        self.forward(MOVE_DISTANCE)

    def at_finish(self) -> bool:
        return self.ycor() > FINISH_LINE_Y
