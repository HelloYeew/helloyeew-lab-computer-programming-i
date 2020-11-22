import sys

def is_triangle(a,b,c):
    if a + b > c:
        if a + c > b:
            if b + c > a:
                print("True")
            else:
                print("False")
        else:
            print("False")
    else:
        print("False")
def read_nonnegative(word):
    num = float(input(word))
    if num<0 :
        print("Invalid value: input must be nonnegative")
        del num
    else :
        return num

# a = read_nonnegative("Enter a nonnegative number: ")
# print(a)
a = float(input("Enter 1st line's length: "))
if a<0:
    print("Invalid value: input must be nonnegative")
    sys.exit()
b = float(input("Enter 2nd line's length: "))
if b<0:
    print("Invalid value: input must be nonnegative")
    sys.exit()
c = float(input("Enter 3rd line's length: "))
if c<0:
    print("Invalid value: input must be nonnegative")
    sys.exit()
if a+b>c:
    if a+c>b:
        if b+c>a:
            print("It's a triangle.")
        else:
            print("It's not a triangle.")
    else:
        print("It's not a triangle.")
else:
    print("It's not a triangle.")
