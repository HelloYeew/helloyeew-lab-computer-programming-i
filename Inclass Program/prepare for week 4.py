def print_hello(name):
    # print("Hello," + name) # error cuz + must use string
    print(f"Hello, {name}")

def read_one_int(word):
    num = int(input(word))
    return num

def read_two_ints():
    a = int(input("Enter num:"))
    b = int(input("Enter num2:"))
    return a,b

def read_two_floats():
    num1 = float(input("Enter side1:"))
    num2 = float(input("Enter side2:"))
    return num1,num2

def compute_rectangle_area(side1,side2):
    return side1*side2