import turtle
import random

from matplotlib import colors

screen = turtle.Screen()
screen.setup(600, 600)
screen.bgcolor("white")
screen.title("basic Mandala")
p = ["red", "blue", "green"]

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.width(2)

t.goto(0, 0)

for l in range(50,200,50):

    k = (l//50) - 1
    t.color(p[k])

    for _ in range(12):
        t.left(30)

        for _ in range(4):
            t.left(90)
            t.forward(l)

screen.mainloop()