def sides():
    sides = eval(input("Enter the number of sides your shape has: "))
    import turtle
    screen = turtle.Screen()
    my_turtle = turtle.Turtle()
    my_turtle.width(5)
    my_turtle.color("blue")
    print(screen)
    for i in range(sides):
        i = i
        my_turtle.forward(50)
        my_turtle.left(360/sides)
    turtle.done()

sides()