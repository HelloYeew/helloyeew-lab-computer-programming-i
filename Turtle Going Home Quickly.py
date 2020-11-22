LAB = "turtlelab3.py"
import urllib.request
urllib.request.urlretrieve(f"http://elab.cpe.ku.ac.th/turtlelab/{LAB}",LAB)

from turtlelab3 import turtle,home,check
from math import atan2,pi

angle = (atan2(home.y,home.x))*180/pi
distance = (((home.y)**2)+((home.x)**2))**0.5
turtle.left(angle)
turtle.forward(distance)

check()