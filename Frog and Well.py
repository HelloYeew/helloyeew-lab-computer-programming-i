import sys
depth = int(input("What is the well's depth? "))
jump = int(input("Enter the height the frog can jump up: "))
slip = int(input("Enter the height the frog slips down: "))
step = depth
day = 1
if jump-slip<=0 and jump<depth:
    print("The frog will never escape from the well.")
    sys.exit()
while step>0:
    step = step-jump
    if step <= 0:
        break
    print(f"On day {day} the frog leaps to the depth of {step} meters.")
    step = step+slip
    print(f"At night he slips down to the depth of {step} meters.")
    day+=1
print(f"The frog gets out of the well on day {day}.")