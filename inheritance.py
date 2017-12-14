class Parent():
	def __init__(self, last_name, eye_color):
		print "Parent constructor called"
		self.last_name = last_name
		self.eye_color = eye_color

class Child(Parent):
	def __init__(self, last_name, eye_color, noT):
		print("child constructor called")
		Parent.__init__(self, last_name, eye_color)
		self.noT = noT



#billy_cyrus = Parent("Cyrus", "blue")

#print(billy_cyrus.last_name)

miley_cyrus = Child("Cyrus", "blue", "three")
print(miley_cyrus.last_name)
print(miley_cyrus.noT)