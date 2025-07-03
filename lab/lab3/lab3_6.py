LAB = "turtlelab3.py"
import urllib.request
urllib.request.urlretrieve(f"http://elab.cpe.ku.ac.th/turtlelab/{LAB}.2",LAB)

from turtlelab3 import turtle,home,check
from math import degrees,atan

x, y = home.x, home.y

distance = ((x**2) + (y**2)) ** 0.5
degree = degrees(atan(abs(y/x)))

turtle.right(degree)
turtle.forward(distance)

turtle.done()

check()