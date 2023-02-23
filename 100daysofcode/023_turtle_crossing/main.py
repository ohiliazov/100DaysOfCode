import time
from turtle import Screen

from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player_turtle = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player_turtle.move_forward, "Up")

while True:
    scoreboard.print_level()

    time.sleep(0.1)
    screen.update()
    car_manager.generate_car()
    car_manager.move()

    if car_manager.is_hit_by_car(player_turtle):
        break

    if player_turtle.at_finish():
        player_turtle.move_to_start()
        car_manager.increase_speed()
        scoreboard.next_level()

screen.update()
scoreboard.game_over()
screen.exitonclick()
