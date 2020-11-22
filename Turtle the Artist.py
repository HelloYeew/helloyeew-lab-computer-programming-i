LAB = "turtlelab7.py"
import urllib.request
urllib.request.urlretrieve(f"http://elab.cpe.ku.ac.th/turtlelab/{LAB}.3",LAB)

from turtlelab7 import turtle,check

def create_polygon(n,size):
    for i in range (n):
        turtle.forward(size)
        turtle.left(360/n)

check()