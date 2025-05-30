import turtle
from turtle import (right, left, forward, backward, speed, exitonclick, penup, pendown)
# scale = scale for image
# x = cube length
# y = turn (45 degree increments)
# z = diagonol cube length
scale=1
x=100*scale
y=45
z=71*scale
# cube1 = base cube
# nose = nose spiral/loop
# reset = reset position from end of cube to beginning of cube
def cube (offset):
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
    forward(z-(offset*scale))
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
# def nose(loops, distance, angle):
#   for i in range(loops):
#     for _ in range(2):
#       length = i*distance
#       turtle.forward(length)
#       turtle.left(angle)
def reset ():
    right(y*4)
    forward(z)
    left(3*y)
# prep
speed(10)
penup()
backward(50*scale)
right(2*y)
forward(200*scale)
left(2*y)
pendown()
#smile
cube(0)
reset()
cube(0)
reset()
right(4*y)
forward(x*3)
right(4*y)
cube(1)
reset()
penup()
backward(2*x)
left(2*y)
forward(x)
right(2*y)
pendown()
cube(0)
reset()
forward(3*x)
cube(0)
reset()
#eye 1
penup()
backward(4*x)
left(2*y)
forward(2*x)
right(2*y)
pendown()
cube(1)
reset()
backward(x)
left(2*y)
forward(x)
right(2*y)
cube(0)
reset()
#eye 2
penup()
right(2*y)
forward(x)
left(2*y)
forward(x)
pendown()
cube(0)
reset()
backward(x)
left(2*y)
forward(x)
right(2*y)
cube(0)
reset()
# # # nose prep
# penup()
# right(2*y)
# forward(x)
# right(2*y)
# forward(1.5*x)
# left(2*y)
# forward(0.5*x)
# # # nose
# pendown()
# nose(50,1,90)
#done
penup()
left(2*y)
forward(10*x)

exitonclick()