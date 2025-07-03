LAB = "turtlelab7.py"
import urllib.request
urllib.request.urlretrieve(f"http://elab.cpe.ku.ac.th/turtlelab/{LAB}.3",LAB)

from turtlelab7 import turtle,check

def create_polygon(n,size):
    """commands the Turtle to create a regular polygon of n sides with the size specified"""
    rotate_deg = 360 // n
    for _ in range(n):
        turtle.forward(size)
        turtle.left(rotate_deg)


check()