import math

def check_unit(area):
    """Check plural (square meter or square meters)"""
    if area > 1:
        return "square meters"
    else:
        return "square meter"


def cal_circle(r):
    """Calculate and return area result)"""
    return math.pi * r * r


def cal_triangle(b, h):
    """Calculate and return area result)"""
    return 0.5 * b * h


def cal_rectangle(w, h):
    """Calculate and return area result)"""
    return w * h


def print_result(answer, shape, unit):
    """Print the area result with correct unit(s)"""
    print(f'Area of this {shape} is {answer: .2f} {unit}.')

# menu = input("(T)riangle (R)ectangle (C)ircle : ")
# if menu == "T" or menu == "t":
#     b = float(input("base = "))
#     h = float(input("height = "))
#     ans = cal_triangle(b, h)
#     print_result(ans, "triangle", check_unit(ans))
#
# elif menu == "R" or menu == "r":
#     w = float(input("width = "))
#     h = float(input("height = "))
#     ans = cal_rectangle(w, h)
#     print_result(ans, "rectangle", check_unit(ans))
#
# elif menu == "C" or menu == "c":
#     r = float(input("Radius = "))
#     ans = cal_circle(r)
#     print_result(ans, "circle", check_unit(ans))
#
# else:
#     print("Incorrect Input!")

while True:
    menu = input("(T)riangle (R)ectangle (C)ircle (Q)uit : ")
    if menu == "T" or menu == "t":
        b = float(input("base = "))
        h = float(input("height = "))
        ans = cal_triangle(b, h)
        print_result(ans, "triangle", check_unit(ans))
    elif menu == "R" or menu == "r":
        w = float(input("width = "))
        h = float(input("height = "))
        ans = cal_rectangle(w, h)
        print_result(ans, "rectangle", check_unit(ans))
    elif menu == "C" or menu == "c":
        r = float(input("Radius = "))
        ans = cal_circle(r)
        print_result(ans, "circle", check_unit(ans))
    elif menu == "Q" or menu == "q":
        print ("Bye")
        break
    else:
        print("Incorrect Input!")