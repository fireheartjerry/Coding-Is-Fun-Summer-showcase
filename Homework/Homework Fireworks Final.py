from turtle import *
from random import *
bgcolor("black")
penup()
goto(-50,-300)
width(10)
color("grey")
forward(100)
left(90)
forward(56)
left(90)
forward(100)
left(90)
forward(56)

penup()
goto(-200,-200)
pendown()
color("red")
begin_fill()
forward(100)
left(90)
forward(25)
left(90)
forward(100)
left(90)
forward(25)
end_fill()
color("orange")
penup()
goto(-188,-193)
pendown()
left(270)
forward(20)
color("grey")
forward(1)

firework = Turtle()
firework.shape("triangle")
firework.shapesize(1.3)
firework.color("white")
firework.pencolor("white")
firework.penup()
firework.hideturtle()
firework.goto(-188,-174)
firework.showturtle()
firework.pendown()
firework.left(90)
firework.width(5)
for i in range(110):
    color_select = randint(1,6)
    firework.speed(0)
    firework.forward(4)
    firework.right(0.51)
    color_select = randint(1,6)
    if color_select == 1:
        firework.color("red")
    elif color_select == 2:
        firework.color("orange")
    elif color_select == 3:
        firework.color("yellow")
    elif color_select == 4:
        firework.color("green")
    elif color_select == 5:
        firework.color("blue")
    elif color_select == 6:
        firework.color("purple")
firework.shape("triangle")
speed(0)
for i in range(1,74):
    speed(0)
    explosion = firework.clone()
    explosion.shapesize(0.3*i)
    color_select = randint(1,6)
    if color_select == 1:
        explosion.color("red")
    elif color_select == 2:
        explosion.color("orange")
    elif color_select == 3:
        explosion.color("yellow")
    elif color_select == 4:
        explosion.color("green")
    elif color_select == 5:
        explosion.color("blue")
    elif color_select == 6:
        explosion.color("purple")
    firework.left(7.5)
done()