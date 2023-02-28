import json
import turtle
from typing import List, Tuple

import pandas as pd
from shapely import Polygon

df = pd.read_csv("30_states.csv", converters={"poly": json.loads})

ALL_OBLASTS = {region: Polygon(poly) for _, region, poly in df.values}


screen = turtle.Screen()
screen.setup(width=1000, height=1000)
screen.tracer(0)
screen.bgcolor("lightgrey")

painter = turtle.Turtle(visible=False)
painter.speed("fastest")
painter.color("grey", "lightblue")


def draw_polygon(coords: List[Tuple[float, float]]):
    x, y = coords[0]
    painter.goto(x, y)
    painter.pendown()
    painter.begin_fill()
    for x, y in coords[1:]:
        painter.goto(x, y)
    painter.penup()
    painter.end_fill()


for region, poly in ALL_OBLASTS.items():
    draw_polygon(poly.exterior.coords)

painter.fillcolor("lightgreen")

writer = turtle.Turtle(visible=False)
writer.penup()

total_states = len(ALL_OBLASTS)
found = set()
while len(found) < total_states:
    guess = screen.textinput(
        title=f"Знайдено {len(found)}/{total_states} областей",
        prompt="Яка наступна область України?",
    )

    if guess is None:
        break

    if guess in found or guess not in ALL_OBLASTS:
        continue

    poly: Polygon = ALL_OBLASTS[guess]
    draw_polygon(poly.exterior.coords)
    found.add(guess)
    for oblast, poly in ALL_OBLASTS.items():
        if oblast in found:
            writer.goto(poly.centroid.x, poly.centroid.y)
            writer.write(oblast, align="center", font=("Courier", 12, "bold"))

writer.pencolor("red")

missing = [oblast for oblast in ALL_OBLASTS.keys() if oblast not in found]

for oblast in missing:
    center = ALL_OBLASTS[oblast].centroid
    writer.goto(center.x, center.y)
    writer.write(oblast, align="center", font=("Courier", 10, "normal"))

screen.exitonclick()
