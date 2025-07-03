import os 
import turtle as tl 
import urllib.request

LAB = "turtlelab1.py"

if not os.path.exists("turtlelab1.py"):
    urllib.request.urlretrieve(f"http://elab.cpe.ku.ac.th/turtlelab/{LAB}.7",LAB)
else:
    print(f"File {LAB} already exists, skipping download.")

from turtlelab1 import turtle,check

turtle.right(45)
turtle.forward(350)
turtle.right(90 + 45)
turtle.forward(350)
turtle.right(90)
turtle.forward(50)

turtle.done()

check()