# Turtle fireworks
from turtle import *
from time import *
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
forward(100)
left(90)
forward(25)
left(90)
forward(100)
left(90)
forward(25)
begin_fill()
goto(-200,-200)
goto(-200,-300)
goto(-175,-300)
goto(-175,-200)
goto(-200,-200)
end_fill()
color("orange")
penup()
goto(-188,-193)
pendown()
left(270)
forward(20)
sleep(0.25)
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
for i in range(100):
    color_select = randint(1,6)
    firework.speed(0)
    firework.forward(4.5)
    firework.right(0.5)
    color_select = randint(1,6)
    if color_select == 1:
        firework.color("red")
    elif color_select == 2:
        firework.color("blue")
    elif color_select == 3:
        firework.color("green")
    elif color_select == 4:
        firework.color("yellow")
    elif color_select == 5:
        firework.color("purple")
    elif color_select == 6:
        firework.color("magenta")
for i in range(1,63):
    firework.shape("circle")
    firework.shapesize(i)
    firework.speed(0)
    color_select = randint(1,6)
    if color_select == 1:
        firework.color("red")
    elif color_select == 2:
        firework.color("blue")
    elif color_select == 3:
        firework.color("green")
    elif color_select == 4:
        firework.color("yellow")
    elif color_select == 5:
        firework.color("purple")
    elif color_select == 6:
        firework.color("magenta")
for i in range(63,1,-1):
    firework.shape("circle")
    firework.shapesize(i)
    firework.speed(0)
    color_select = randint(1,6)
    if color_select == 1:
        firework.color("red")
    elif color_select == 2:
        firework.color("blue")
    elif color_select == 3:
        firework.color("green")
    elif color_select == 4:
        firework.color("yellow")
    elif color_select == 5:
        firework.color("purple")
    elif color_select == 6:
        firework.color("magenta")
for i in range(1,63):
    firework.shape("circle")
    firework.shapesize(i*7)
    firework.speed(0)
    color_select = randint(1,6)
    if color_select == 1:
        firework.color("red")
    elif color_select == 2:
        firework.color("blue")
    elif color_select == 3:
        firework.color("green")
    elif color_select == 4:
        firework.color("yellow")
    elif color_select == 5:
        firework.color("purple")
    elif color_select == 6:
        firework.color("magenta")
sleep(3)

