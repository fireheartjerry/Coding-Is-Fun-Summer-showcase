import turtle
turtle_screen = turtle.Screen()
my_turtle = turtle.Turtle()
my_turtle.shape("turtle")
my_turtle.forward(100)
my_turtle.right(90)
my_turtle.backward(100)

for i in range(4):
    my_turtle.left(90)
    my_turtle.forward(10)

my_turtle.goto(30,30)
my_turtle.forward(120)
my_turtle.left(120)
my_turtle.forward(120)
my_turtle.left(120)
my_turtle.forward(120)


turtle.done()
