import math


def check_unit(number):
    """
    The function that check the number and return the unit

    Parameter:
    number (float) : the answer from calculation

    Return:
    The unit of the answer

    """
    # check if the values is greater than one.
    if(number > 1):
        # return the unit with "s"
        return "square meters"
    else:
        # otherwise return unit without "s"
        return "square meter"


def print_result(shape, number, unit):
    """ 
    The function that print the result with a conditional format.

    Parameter:
    shape (str) : The name of the shape
    number (flaot) : The answer from calculation
    unit (str) : The answer unit


    """

    print(f"Area of {shape} is {number:.2f} {unit}")


def cal_triangle(base, width):
    """
    The function that compute the triangle area.

    Parameter:
    base (float) : The base of the triangle
    width (float) : The width of the triangle

    Return:
    The area of the triangle

    """

    return 1/2*base*width


def cal_rectangle(height, width):
    """
    The function that compute the rectangle area.

    Parameter:
    height (float) : The height of the rectangle
    width (float) : The width of the rectangle

    Return:
    The area of the rectangle

    """

    return height*width


def cal_circle(radius):
    """
    The function that compute the circle area.

    Parameter:
    radius (float) : The radius of the circle

    Return:
    The area of the circle

    """

    return math.pi * radius**2

# Main code


while True:
    menu = input("(T)riangle (R)ectangle (C)ircle (Q)uit : ")
    if(menu.lower() == "t"):
        base_t = float(input("base = "))
        width_t = float(input("width = "))
        area = cal_triangle(base_t, width_t)
        print_result("triangle", area, check_unit(area))
    elif(menu.lower() == "r"):
        height_r = float(input("height = "))
        width_r = float(input("width = "))
        area = cal_rectangle(height_r, width_r)
        print_result("rectangle", area, check_unit(area))
    elif(menu.lower() == "c"):
        radius_c = float(input("Radius = "))
        area = cal_circle(radius_c)
        print_result("circle", area, check_unit(area))
    elif(menu.lower() == "q"):
        break
    else:
        print("Incorrect Input")
print("Bye")
