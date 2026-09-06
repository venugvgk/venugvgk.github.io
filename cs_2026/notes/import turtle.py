import turtle

screen = turtle.Screen()
screen.title("Concentric Circles")

pen = turtle.Turtle()
pen.speed(0)

for radius in range(20, 201, 20):
	pen.penup()
	pen.goto(0, -radius)
	pen.setheading(0)
	pen.pendown()
	pen.circle(radius)

screen.exitonclick()
