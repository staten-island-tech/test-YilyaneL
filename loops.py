import turtle
from turtle import *
t = Turtle()
t.speed(10)

def square():
    x = 5
    y = 90
    turn = 5
    for i in range(60):
        t.forward(x)
        t.right(y)
        t.forward(x)
        t.right(y)
        t.forward(x)
        t.right(y)
        t.right(turn)
        x = x + 5
square()
t.done()