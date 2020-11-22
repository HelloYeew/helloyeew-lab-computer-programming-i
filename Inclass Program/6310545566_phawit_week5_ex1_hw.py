n = 1
while True:
    num = int(input(f"Enter value{n}: "))
    if num == -99:
        break
    n += 1
print(f"You entered {n-1} numbers.")