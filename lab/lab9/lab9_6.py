LAB = "turtlelab9.py"
import urllib.request
urllib.request.urlretrieve(f"http://elab.cpe.ku.ac.th/turtlelab/{LAB}",LAB)

from turtlelab9 import turtle,check

for _ in range(8):
    for _ in range(5):
        turtle.forward(50)
    for _ in range(5):
        turtle.backward(50)
    turtle.left(45)

check()