LAB = "turtlelab2x.py"
import urllib.request
urllib.request.urlretrieve(f"http://elab.cpe.ku.ac.th/turtlelab/{LAB}",LAB)

from turtlelab2x import turtle,home,shop,check

turtle.forward(shop.x)
turtle.left(90)
turtle.forward(shop.y)
turtle.right(90)
turtle.forward(home.x-shop.x)
turtle.left(90)
turtle.forward(home.y-shop.y)

check()