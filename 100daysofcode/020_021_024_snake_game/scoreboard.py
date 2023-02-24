from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
HIGH_SCORE_PATH = "highscore.txt"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__(visible=False)
        self.speed(0)
        self.goto(0, 260)
        self.color("white")

        self.score = 0
        self.high_score = 0

        self.read_high_score()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(
            f"Score: {self.score} High Score: {self.high_score}",
            align=ALIGNMENT,
            font=FONT,
        )

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def read_high_score(self):
        with open(HIGH_SCORE_PATH) as f:
            self.high_score = int(f.readline())

    def update_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open(HIGH_SCORE_PATH, mode="w") as f:
                f.write(str(self.high_score))

    def reset(self):
        self.update_high_score()
        self.score = 0
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(
            "GAME OVER",
            align=ALIGNMENT,
            font=FONT,
        )
