"""
Specify the properties of your trapezoid.
Enter length of side a: 38
Enter length of side b: 22.4
Enter height: 8.2
The trapezoid area is 247.64
"""
print("Specify the properties of your trapezoid.")
a = float(input("Enter length of side a: "))
b = float(input("Enter length of side b: "))
height = float(input("Enter height: "))
area = ((a+b)/2)*height
print(f"The trapezoid area is {area:.2f}")