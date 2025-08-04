LAB = "turtlelab6.py"
import urllib.request
urllib.request.urlretrieve(f"http://elab.cpe.ku.ac.th/turtlelab/{LAB}.10",LAB)

from turtlelab6 import turtle,home,mozart,flippy,check
from math import sqrt,atan2,degrees

def walkto(x, y):
    """Have Turtle walk straight to location (x,y)"""
    dx = x - turtle.x
    dy = y - turtle.y
    dist = sqrt(dx**2 + dy**2)
    angle = degrees(atan2(dy, dx))
    turtle.left(angle - turtle.heading)
    turtle.forward(dist)

def distance(x1, y1, x2, y2):
    """Return distance between two points"""
    return sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Calculate total distance for both orders
start_x, start_y = 0, 0

# Path A: start → Mozart → Flippy → Home
dist_A = (
    distance(start_x, start_y, mozart.x, mozart.y) +
    distance(mozart.x, mozart.y, flippy.x, flippy.y) +
    distance(flippy.x, flippy.y, home.x, home.y)
)

# Path B: start → Flippy → Mozart → Home
dist_B = (
    distance(start_x, start_y, flippy.x, flippy.y) +
    distance(flippy.x, flippy.y, mozart.x, mozart.y) +
    distance(mozart.x, mozart.y, home.x, home.y)
)

# Choose the shorter path
if dist_A < dist_B:
    walkto(mozart.x, mozart.y)
    walkto(flippy.x, flippy.y)
    walkto(home.x, home.y)
else:
    walkto(flippy.x, flippy.y)
    walkto(mozart.x, mozart.y)
    walkto(home.x, home.y)

check()