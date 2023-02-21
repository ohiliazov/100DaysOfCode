from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__("circle")
        self.penup()
        self.color("white")

        self.x_delta = 10
        self.y_delta = 10
        self.move_speed = 0.05
        self.stopped = True

    def move(self):
        if not self.stopped:
            self.goto(
                x=self.xcor() + self.x_delta,
                y=self.ycor() + self.y_delta,
            )

    def hit_wall(self) -> bool:
        return self.ycor() == 280 or self.ycor() == -280

    def hit_paddle(self, paddle) -> bool:
        return (
            -330 <= self.xcor() <= 330
            and abs(self.xcor() - paddle.xcor()) == 20
            and abs(self.ycor() - paddle.ycor()) <= 50
        )

    def bounce_x(self):
        self.x_delta = -self.x_delta
        self.move_speed *= 0.9

    def bounce_y(self):
        self.y_delta = -self.y_delta
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()
        self.move_speed = 0.05

    def toggle_stop(self):
        self.stopped = not self.stopped
