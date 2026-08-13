import turtle

screen = turtle.Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("basic Mandala")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.width(2)
t.color("white")

t.goto(0, 0)

for l in range(0,200,25):

    for _ in range(6):
        t.left(60)

        for _ in range(3):
            t.left(120)
            t.forward(l)



screen.mainloop()