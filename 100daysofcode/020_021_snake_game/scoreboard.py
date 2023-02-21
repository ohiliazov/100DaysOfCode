from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__(visible=False)
        self.speed(0)
        self.goto(0, 260)
        self.color("white")

        self.score = 0

        self.print_score()

    def print_score(self):
        self.clear()
        self.write(
            f"Score: {self.score}",
            align=ALIGNMENT,
            font=FONT,
        )

    def increase_score(self):
        self.score += 1
        self.print_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(
            f"GAME OVER",
            align=ALIGNMENT,
            font=FONT,
        )
