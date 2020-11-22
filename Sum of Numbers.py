number = []
while True:
    num = float(input("Enter a number (to exit, just enter 0): "))
    if num == 0:
        break
    else:
        number.append(num)
pos = 0
neg = 0
for i in range(len(number)):
    if number[i] > 0:
        pos = pos+number[i]
    else:
        neg = neg+number[i]
print(f"Sum of positive numbers is {pos:.2f}")
print(f"Sum of negative numbers is {neg:.2f}")