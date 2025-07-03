LAB = "turtlelab4.py"
import urllib.request
urllib.request.urlretrieve(f"http://elab.cpe.ku.ac.th/turtlelab/{LAB}.0",LAB)

from turtlelab4 import turtle,check

def draw_square(size):
    """Commands the Turtle to draw a square of the size specified"""
    for _ in range(4):
        turtle.forward(size)
        turtle.left(90)

def draw_triangle(size):
    """Commands the Turtle to draw a triangle of the size specified"""
    for _ in range(3):
        turtle.forward(size)
        turtle.left(120)


turtle.left(30)
draw_square(120)
turtle.left(90)
turtle.forward(120)
turtle.right(90)
draw_triangle(120)
turtle.done()

check()