import turtle
from turtle import *
t = Turtle()
t.speed(0)
"""
def square():
    x = 5
    y = 90
    turn = 5
    for i in range(60):
        t.forward(x)
        t.left(y)
        t.forward(x)
        t.left(y)
        t.forward(x)
        t.left(y)
        t.forward(x)
        t.left(y)
        t.right(turn)
        x = x + 5
square()
"""

def star():
    x = 5
    y = 144
    turn = 5
    for i in range(60):
        t.forward(x)
        t.left(y)
        t.forward(x)
        t.left(y)
        t.forward(x)
        t.left(y)
        t.forward(x)
        t.left(y)
        t.forward(x)
        t.left(y)
        t.right(turn)
        x = x + 5
star()
t.done()