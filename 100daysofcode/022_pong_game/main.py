import time
from turtle import Screen

from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

right_paddle = Paddle(x_pos=350, y_pos=0)
left_paddle = Paddle(x_pos=-350, y_pos=0)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")
screen.onkey(ball.toggle_stop, "space")

while not scoreboard.game_over():
    time.sleep(ball.move_speed)
    scoreboard.print_score()
    screen.update()

    if ball.hit_wall():
        ball.bounce_y()

    if ball.hit_paddle(right_paddle) or ball.hit_paddle(left_paddle):
        ball.bounce_x()

    if ball.xcor() == 380:
        ball.reset_position()
        scoreboard.score_left()

    if ball.xcor() == -380:
        ball.reset_position()
        scoreboard.score_right()

    ball.move()

scoreboard.print_score()
scoreboard.print_winner()

screen.exitonclick()
