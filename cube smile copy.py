import turtle
from turtle import (right, left, forward, backward, speed, exitonclick, penup, pendown)
# x = cube length
# y = turn (45 degree increments)
# z = diagnol cube length
scale=1
x=100*scale
y=45
z=71*scale
speed(10)
def cube1 ():
    for i in range(4):
        forward(x)
        left(2*y)
    penup()
    forward(0.5*x)
    left(2*y)
    forward(0.5*x)
    pendown()
    for i in range(3):
        forward(x)
        right(2*y)
    forward(x)
    left(y)
    for i in range(4):
        forward(z)
        right(y)
        
    speed(1)

    forward(z)
    right(3*y)

    forward(x)
    right(y)

    forward(z)
    right(y)

    forward(x)
    right(3*y)

    forward(z)
    left(y)
    forward(x)
    left(3*y)
    forward(z)


cube1()

exitonclick()