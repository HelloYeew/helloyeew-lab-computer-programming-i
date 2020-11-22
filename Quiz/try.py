import math,sys
def check(a):
    num = float(a)

while True:
    inputt = str(input("(T)riangle (R)ectangle (C)ircle (Q)uit : "))
    if inputt == "T" or inputt == "t":
        while True:
            b = input("base = ")
            if b != float(b):
                break
            else:
                print("Please enter a number!")
        h = float(input("height = "))
        area = 0.5*b*h
        if area>1:
            print(f"Area of this triangle is {area:.2f} square meters.")
        else:
            print(f"Area of this triangle is {area:.2f} square meter.")
    elif inputt == "R" or inputt == "r":
        w = float(input("width = "))
        h = float(input("height = "))
        area = w*h
        if area>1:
            print(f"Area of this rectangle is {area:.2f} square meters.")
        else:
            print(f"Area of this rectangle is {area:.2f} square meter.")
    elif inputt == "C" or inputt == "c":
        r = float(input("Radius = "))
        area = math.pi*r*r
        if area>1:
            print(f"Area of this circle is {area:.2f} square meters.")
        else:
            print(f"Area of this circle is {area:.2f} square meter.")
    elif inputt == "Q" or inputt == "q":
        print("Bye")
        sys.exit()
    else:
        print("Incorrect Input")