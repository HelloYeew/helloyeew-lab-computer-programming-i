LAB = "turtlelab2.py"
import urllib.request
urllib.request.urlretrieve(f"http://elab.cpe.ku.ac.th/turtlelab/{LAB}",LAB)

from turtlelab2 import turtle,home,check

turtle.forward(home.x)
turtle.left(90)
turtle.forward(home.y)

check()