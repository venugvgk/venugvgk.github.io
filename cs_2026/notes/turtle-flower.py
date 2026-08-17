import turtle
screen = turtle.Screen()
t = turtle.Turtle()
t.speed(3)
cl = ["red", "green", "blue"]

for i in range(9):
    t.color(cl[i%3])
    t.left(10)
    t.circle(100,90)
    t.left(90)
    t.circle(100,90)

screen.mainloop()
