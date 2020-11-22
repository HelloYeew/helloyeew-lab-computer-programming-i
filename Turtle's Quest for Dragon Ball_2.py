LAB = "turtlelab8.py"
import urllib.request

urllib.request.urlretrieve(f"http://elab.cpe.ku.ac.th/turtlelab/{LAB}", LAB)

from turtlelab8 import turtle, radar, check

def reset_heading():
    current_heading = turtle.heading
    if current_heading > 180:
        turtle.left(360 - current_heading)
    elif current_heading < 180:
        turtle.right(current_heading)
    else:
        turtle.left(160)


def set_heading():
    current_state = radar.ball_direction()
    if current_state == "ne":
        turtle.left(22.5)
    elif current_state == "n":
        turtle.left(67.5)
    elif current_state == "nw":
        turtle.left(112.5)
    elif current_state == "w":
        turtle.left(157.5)
    elif current_state == "sw":
        turtle.right(112.5)
    elif current_state == "s":
        turtle.right(67.5)
    elif current_state == "se":
        turtle.right(22.5)


while radar.ball_direction() != "x":
    current_state = radar.ball_direction()
    set_heading()
    while current_state == radar.ball_direction():
        turtle.forward(5)
    reset_heading()

check()