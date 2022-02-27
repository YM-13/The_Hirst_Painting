
import random

rgb_colors = [(245, 243, 237), (248, 241, 244), (238, 240, 246), (201, 164, 112), (239, 246, 241), (152, 75, 50),
              (221, 201, 138)]

import turtle
from turtle import Screen, Turtle

tim = Turtle()
turtle.colormode(255)
tim.hideturtle()
tim.penup()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)


for _ in range(10):
	tim.dot(20, random.choice(rgb_colors))
	tim.forward(50)

for _ in range(10):
	tim.setheading(90)
	tim.forward(50)
	tim.setheading(180)
	tim.forward(500)
	tim.setheading(0)
	for _ in range(10):
		tim.dot(20, random.choice(rgb_colors))
		tim.forward(50)


screen = Screen()
screen.exitonclick()
