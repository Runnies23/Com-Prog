LAB = "turtlelab2.py"
import urllib.request
urllib.request.urlretrieve(f"http://elab.cpe.ku.ac.th/turtlelab/{LAB}.4",LAB)

from turtlelab2 import turtle,home,check

if home.x < 0:
    turtle.left(180)
turtle.forward(abs(home.x))
if home.y < 0:
    turtle.left(90)
turtle.forward(abs(home.y))

turtle.done()
check()