import math

x = float(input("Enter x: "))
y = float(input("Enter y: "))
d = float(input("Enter d: "))
pond = math.pi*((d/2)**2)
lawn = x*y
answer = lawn-pond
print(f"The area of the lawn is {answer:.2f} sq.m.")