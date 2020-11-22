# Enter length of side 1: 3
# Enter length of side 2: 4
# Enter length of side 3: 5
# Area of the triangle is 6.00

a = float(input("Enter length of side 1: "))
b = float(input("Enter length of side 2: "))
c = float(input("Enter length of side 3: "))
s = (a+b+c) / 2
area = (s * (s-a) * (s-b) * (s-c))**0.5
print(f"Area of the triangle is {area:.2f}")