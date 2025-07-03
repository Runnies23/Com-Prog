LAB = "turtlelab6.py"
import urllib.request
urllib.request.urlretrieve(f"http://elab.cpe.ku.ac.th/turtlelab/{LAB}.10",LAB)

from turtlelab6 import turtle,home,mozart,flippy,check
from math import sqrt,atan2,degrees

def walkto(x,y):
    """Have Turtle walk straight to location (x,y)"""
    dx = x - turtle.x
    dy = y - turtle.y
    dist = sqrt(dx**2 + dy**2)
    angle = degrees(atan2(dy,dx))
    turtle.left(angle-turtle.heading) # Turtle's current heading may not be 0
    turtle.forward(dist)

walkto(mozart.x,mozart.y)
walkto(flippy.x,flippy.y)
walkto(home.x,home.y)

check()