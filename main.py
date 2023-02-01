import random
import turtle
from turtle import Turtle, Screen

import colorgram

turtle.colormode(255)

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

tim = Turtle()
tim.speed(0)
tim.penup()
tim.hideturtle()
tim.setposition(-225, -225)


def line():
    for i in range(10):
        tim.dot(20, random.choice(rgb_colors))
        tim.forward(50)


for _ in range(10):
    line()
    tim.left(90)
    tim.forward(50)
    tim.right(90)
    tim.back(500)

screen = Screen()
screen.exitonclick()
