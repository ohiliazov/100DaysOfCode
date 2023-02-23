import random
from turtle import Turtle

from shapely import Polygon

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

X_START = 325
X_END = -325
Y_TOP = 250
Y_END = -250


class Car(Turtle):
    def __init__(self):
        super().__init__("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.speed(0)
        self.penup()
        self.color(random.choice(COLORS))
        self.goto(X_START, random.randint(Y_END, Y_TOP))

    def hit_player(self, player: Turtle):
        car_poly = Polygon(
            [(x + self.xcor(), y + self.ycor()) for y, x in self.get_shapepoly()]
        )
        player_poly = Polygon(
            [(x + player.xcor(), y + player.ycor()) for x, y in player.get_shapepoly()]
        )

        intersects = car_poly.intersects(player_poly)
        return intersects


class CarManager:
    def __init__(self):
        self.cars = []
        self.move_distance = STARTING_MOVE_DISTANCE

    def generate_car(self):
        if random.randint(1, 6) == 1:
            self.cars.append(Car())

    def move(self):
        for car in self.cars:
            car.backward(self.move_distance)
        self.cars = [car for car in self.cars if car.xcor() >= X_END]

    def is_hit_by_car(self, player: Turtle):
        return any(car.hit_player(player) for car in self.cars)

    def increase_speed(self):
        self.move_distance += MOVE_INCREMENT
