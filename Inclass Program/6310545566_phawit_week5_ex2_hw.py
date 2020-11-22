n = 1
sum = 0
while True:
    num = int(input(f"Enter value{n}: "))
    if num == -99:
        break
    n += 1
    sum = sum+num
print(f"You entered {n-1} numbers.")
print(f"Sum of them = {sum}")