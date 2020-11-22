def read_two_floats():
    num1 = float(input("Enter side1:"))
    num2 = float(input("Enter side2:"))
    return num1,num2

def compute_rectangle_area(side1,side2):
    return side1*side2

def compute_perimeter_area(side1,side2):
    return (side1+side2)*2

def area_or_perimeter():
    ans = str(input("Area (A) or Perimeter (P)? "))
    return ans

side1,side2 = read_two_floats()
way = area_or_perimeter()
if way == "A":
    area = compute_rectangle_area(side1,side2)
    print(f"Area is {area:.2f}")
else:
    per = compute_perimeter_area(side1,side2)
    print(f"Perimeter is {per:.2f}")