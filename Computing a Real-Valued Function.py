x = float(input("Enter x: "))
y = float(input("Enter y: "))
if x<=20 and x>5:
    answer = (4*x*y)+5
else:
    answer = (x**2)-(100*y)
print(f"f({x:.3f},{y:.3f}) = {answer:.3f}")
