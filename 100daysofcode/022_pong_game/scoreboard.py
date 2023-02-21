from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__(visible=False)
        self.color("white")
        self.penup()
        self.left_score = 0
        self.right_score = 0
        self.goto(0, 150)

    def print_score(self):
        self.clear()
        self.write(
            f"{self.left_score}  {self.right_score}",
            align="center",
            font=("Courier", 72, "normal"),
        )

    def score_left(self):
        self.left_score += 1

    def score_right(self):
        self.right_score += 1

    def game_over(self):
        return self.left_score == 10 or self.right_score == 10

    def print_winner(self):
        self.goto(0, 0)

        winner = "Left" if self.left_score == 10 else "Right"
        self.write(
            f"{winner} player wins!",
            align="center",
            font=("Courier", 32, "bold"),
        )
