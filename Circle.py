import math
def circle_area(r) :
    return math.pi * (r**2)
    print(f"Circle circumference is {circle_circumference(r)}")
def circle_circumference(r) :
    return 2 * math.pi *r
    print(f"Circle area is {circle_area(r)}")
r = float(input("Enter circle radius: "))
print(f"Circle circumference id {circle_circumference(r):.2f}")
print(f"Circle area is {circle_area(r):.2f}")
