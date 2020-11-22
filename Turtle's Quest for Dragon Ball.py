LAB = "turtlelab8.py"
import urllib.request

urllib.request.urlretrieve(f"http://elab.cpe.ku.ac.th/turtlelab/{LAB}", LAB)

from turtlelab8 import turtle, radar, check
from math import atan2, pi

while radar.ball_direction() != "x":
    # heading
    current_angle = turtle.heading
    current = radar.ball_direction()
    if current == "n":
