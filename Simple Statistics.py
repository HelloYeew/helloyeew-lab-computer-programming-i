import sys

number = []
while True:
    num = str(input("Enter a number (to quit, just [Enter]): "))
    if num == "":
        break
    else:
        number.append(num)
if number == []:
    print("Nothing to do.")
    sys.exit()
for i in range (len(number)):
    number[i] = float(number[i])
print(f"The maximum is {max(number):.2f}")
print(f"The minimum is {min(number):.2f}")
print(f"The average is {sum(number)/len(number):.2f}")