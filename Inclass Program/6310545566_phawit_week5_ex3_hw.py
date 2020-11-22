n = 1
sum = 0
list = []
while True:
    num = int(input(f"Enter value{n}: "))
    if num == -99:
        break
    n += 1
    sum = sum+num
    list.append(num)
print(list)
print(f"{sum/len(list):.2f}")