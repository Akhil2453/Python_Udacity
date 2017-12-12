import turtle

def square():
	window = turtle.Screen()
	window.bgcolor("red")

	Max = turtle.Turtle()

	Max.shape("turtle")
	Max.color("green")
	Max.speed(3)

	for i in range(4):
		Max.forward(100)
		Max.right(90)

	window.exitonclick()

square()