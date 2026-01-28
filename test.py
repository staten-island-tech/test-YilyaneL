import turtle
from turtle import *
t = Turtle()
"""
def rectangle():
    t.forward(125)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(125)
    t.right(90)
    t.forward(100)
rectangle()
"""

def tri(x):
    t.forward(x)
    t.right(120)
    t.forward(x)
    t.right(120)
    t.forward(x)
tri(90)

Turtle.done()