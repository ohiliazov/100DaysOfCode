from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        for x, y in STARTING_POSITION:
            self.add_segment(x, y)

    def add_segment(self, x: int, y: int):
        segment = Turtle(shape="square")
        segment.penup()
        segment.color("white")
        segment.goto(x, y)

        self.segments.append(segment)

    @property
    def head(self):
        return self.segments[0]

    @property
    def tail(self):
        return self.segments[-1]

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            x, y = self.segments[seg_num - 1].position()
            self.segments[seg_num].goto(x, y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def hit_the_wall(self):
        x, y = self.head.position()

        return not (-280 <= x <= 280) or not (-280 <= y <= 280)

    def hit_the_tail(self):
        return any(seg.distance(self.head) < 10 for seg in self.segments[1:])

    def extend(self):
        x, y = self.tail.position()
        self.add_segment(x, y)
