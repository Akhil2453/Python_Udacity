import turtle

def square(akhil):
	for i in range(4):
		akhil.forward(100)
		akhil.right(90)

def art():
	win = turtle.Screen()
	win.bgcolor("red")

	judy = turtle.Turtle()
	judy.shape("turtle")
	judy.color("green")
	judy.speed(2)

	square(judy)

	martha = turtle.Turtle()
	martha.shape("arrow")
	martha.color("blue")
	martha.circle(100)

	win.exitonclick()


art()