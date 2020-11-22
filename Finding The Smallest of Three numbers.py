def min_of_three(a,b,c):
    if a <= b and a <= c:
        return a
    elif b <= a and b <= c:
        return b
    elif c <= a and c <= b:
        return c

print(min_of_three(60.7,-10.25,0))
print(min_of_three(0,10.7,5.2))
print(min_of_three(7.2,20,7.2))