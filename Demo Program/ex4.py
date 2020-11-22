def read_two_floats():
    num1 = float(input("Enter side1:"))
    num2 = float(input("Enter side2:"))
    return num1,num2

def compute_rectangle_area(side1,side2):
    return side1*side2

side1,side2 = read_two_floats()
print(f"Area is {compute_rectangle_area(side1,side2):.2f}")