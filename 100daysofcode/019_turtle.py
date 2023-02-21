import random
from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(
    "Make your bet", "Which turtle wins the race? Enter a color: "
)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [150, 90, 30, -30, -90, -150]

turtles = []
for i in range(6):
    tim = Turtle(shape="turtle")
    tim.color(colors[i])
    tim.penup()
    tim.setposition(x=-230, y=y_positions[i])
    turtles.append(tim)

winner = None
while True:
    turtle: Turtle = random.choice(turtles)
    turtle.forward(random.randint(0, 10))
    if turtle.position()[0] >= 230:
        winner = turtle.pencolor()
        break

if winner == user_bet:
    print(f"You've won! The {winner} turtle is the winner!")
else:
    print(f"You've lost! The {winner} turtle is the winner!")

screen.exitonclick()
