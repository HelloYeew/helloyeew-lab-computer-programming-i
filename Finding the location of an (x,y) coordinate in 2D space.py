# Input a point (x,y):
# x = ? 1.5
# y = ? 2
# The point (1.50,2.00) is in quadrant 1.
print("Input a point (x,y):")
x = float(input("x = ? "))
y = float(input("y = ? "))
if x==0 and y==0:
    print(f"The point ({x:.2f},{y:.2f}) is at the origin.")
elif x>0 and y>0:
    print(f"The point ({x:.2f},{y:.2f}) is in quadrant 1.")
elif x<0 and y>0:
    print(f"The point ({x:.2f},{y:.2f}) is in quadrant 2.")
elif x<0 and y<0:
    print(f"The point ({x:.2f},{y:.2f}) is in quadrant 3.")
elif x>0 and y<0:
    print(f"The point ({x:.2f},{y:.2f}) is in quadrant 4.")
elif x!=0 and y==0:
    print(f"The point ({x:.2f},{y:.2f}) is on the x-axis.")
elif x==0 and y!=0:
    print(f"The point ({x:.2f},{y:.2f}) is on the y-axis.")