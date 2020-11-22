# Enter 1st line's length: 8
# Enter 2nd line's length: 2
# Enter 3rd line's length: 5
# It's not a triangle.
a = float(input("Enter 1st line's length: "))
b = float(input("Enter 2nd line's length: "))
c = float(input("Enter 3rd line's length: "))
if a+b>c:
    if a+c>b:
        if b+c>a:
            if (c**2)==(a**2)+(b**2) or (a**2)==(b**2)+(c**2) or (b**2)==(a**2)+(c**2):
                print("It's a right triangle.")
            else:
                print("It's a triangle but not a right triangle.")
        else:
            print("It's not a triangle.")
    else:
        print("It's not a triangle.")
else:
    print("It's not a triangle.")