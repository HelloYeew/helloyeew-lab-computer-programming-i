LAB = "turtlelab4.py"
import urllib.request
urllib.request.urlretrieve(f"http://elab.cpe.ku.ac.th/turtlelab/{LAB}",LAB)

from turtlelab4 import turtle,check

def draw_square(size):
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(90)


def draw_triangle(size):
    turtle.right(90)
    turtle.forward(size)
    turtle.right(120)
    turtle.forward(size)
    turtle.right(120)
    turtle.forward(size)
    turtle.right(120)

# turtle.left(30)
# draw_square(120)
# turtle.left(90)
# turtle.forward(120)
# turtle.right(90)
# draw_triangle(120)

# check()