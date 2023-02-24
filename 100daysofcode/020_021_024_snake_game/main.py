import time
from turtle import Screen

from food import Food
from scoreboard import Scoreboard
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
scoreboard.update_scoreboard()

screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    for _ in range(15):
        screen.update()
        time.sleep(0.01)
    snake.move()

    if food.distance(snake.head) < 15:
        snake.extend()
        food.refresh()
        scoreboard.increase_score()

    if snake.hit_the_wall() or snake.hit_the_tail():
        # game_is_on = False
        scoreboard.reset()
        snake.reset()

screen.exitonclick()
