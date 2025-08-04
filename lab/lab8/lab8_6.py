LAB = "turtlelab8.py"
import urllib.request
urllib.request.urlretrieve(f"http://elab.cpe.ku.ac.th/turtlelab/{LAB}",LAB)

from turtlelab8 import turtle,radar,check

direction = radar.ball_direction().lower()

while direction != "x":
    match direction:
        case "n":
            turtle.left(90)
            turtle.forward(1)
            turtle.right(90)
        case "s":
            turtle.right(90)
            turtle.forward(1)
            turtle.left(90)
        case "e":
            turtle.forward(1)
        case "w":
            turtle.left(180)
            turtle.forward(1)
            turtle.right(180)
        case "ne":
            turtle.left(45)
            turtle.forward(1)
            turtle.right(45)
        case "nw":
            turtle.left(90 + 45)
            turtle.forward(1)
            turtle.right(90 + 45)
        case "se":
            turtle.right(45)
            turtle.forward(1)
            turtle.left(45)
        case "sw":
            turtle.right(90 + 45)
            turtle.forward(1)
            turtle.left(90 + 45)

    direction = radar.ball_direction().lower()
    

turtle.done()
check()
