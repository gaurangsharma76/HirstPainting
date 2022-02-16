import turtle

import colorgram
from turtle import Turtle, Screen
import random

rgb = []
'''Extracting color from image using colorgram'''
turtle.colormode(255)
colors = colorgram.extract("image.jpg", 30)
for clrs in colors:
    r = clrs.rgb.r
    g = clrs.rgb.g
    b = clrs.rgb.b
    clr = (r, g, b)
    rgb.append(clr)

tur = Turtle()
tur.penup()
tur.hideturtle()
tur.setheading(200)
tur.forward(450)
tur.setheading(0)
tur.speed("fastest")
tur.forward(50)
no_of_dots = 100
for i in range(1, no_of_dots+1):
    clr = random.choice(rgb)
    tur.dot(20, clr)
    tur.forward(50)
    if i % 10 == 0:
        tur.left(90)
        tur.forward(50)
        tur.left(90)
        tur.forward(500)
        tur.left(180)

screen = Screen()
screen.exitonclick()
