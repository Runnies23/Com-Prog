LAB = "turtlelab5.py"
import urllib.request
urllib.request.urlretrieve(f"http://elab.cpe.ku.ac.th/turtlelab/{LAB}.9",LAB)

from turtlelab5 import turtle,mario,check
from math import degrees,atan

x, y = mario.x, mario.y

quatide = 99
if x > 0 and y < 0:
    quatide = 0
elif x < 0 and y < 0:
    quatide = 1
elif x < 0 and y > 0:
    quatide = 2
else:
    quatide = 3

distance = ((x**2) + (y**2)) ** 0.5
degree = degrees(atan(abs(y/x)))

if x < 0:
    turtle.left(180)

if quatide == 1 or quatide == 3:
    turtle.left(degree)
else: 
    turtle.right(degree)

turtle.forward(distance)
turtle.done()

check()