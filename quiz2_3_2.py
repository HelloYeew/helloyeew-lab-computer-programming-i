import math
#Method 2 try except --> Recommended

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


def cal_triangle():
    """
    The function that get the user input and compute the triangle area.

    Return:
    The area of the triangle

    """

    while True:
        try:
            base_t = float(input("base = "))
        except ValueError:
            print("Please Enter Number!")
        else:
            while True:
                try:
                    width_t = float(input("width = "))
                except ValueError:
                    print("Please Enter Number!")
                else:
                    return base_t * width_t * 1/2


def cal_rectangle():
    """
    The function that compute the rectangle area.

    Parameter:
    height (float) : The height of the rectangle
    width (float) : The width of the rectangle

    Return:
    The area of the rectangle

    """
    while True:
        try:
            height_r = float(input("height = "))
        except ValueError:
            print("Please Enter Number!")
        else:
            while True:
                try:
                    width_r = float(input("width = "))
                except ValueError:
                    print("Please Enter Number!")
                else:
                    return height_r * width_r


def cal_circle():
    """
    The function that compute the circle area.

    Parameter:
    radius (float) : The radius of the circle

    Return:
    The area of the circle

    """

    while True:
        try:
            radius_c = float(input("Radius = "))
        except ValueError:
            print("Please Enter Number!")
        else:
            return math.pi * radius_c**2

# Main code

while True:
    menu = input("(T)riangle (R)ectangle (C)ircle (Q)uit : ")
    if(menu.lower() == "t"):
        area_t = cal_triangle()
        print_result("triangle", area_t, check_unit(area_t))
    elif(menu.lower() == "r"):
        area_r = cal_rectangle()
        print_result("rectangle", area_r, check_unit(area_r))
    elif(menu.lower() == "c"):
        area_c = cal_circle()
        print_result("circle", area_c, check_unit(area_c))
    elif(menu.lower() == "q"):
        break
    else:
        print("Incorrect Input")
print("Bye")


