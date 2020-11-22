# What is your weight (kg)? 65
# What is your height (cm)? 175
# BMI: 21.22
# Weight status: normal
weight = int(input("What is your weight (kg)? "))
height = int(input("What is your height (cm)? "))
BMI = weight / ((height/100)**2)
if BMI >= 30:
    status = "obese"
elif BMI < 30 and BMI >= 25:
    status = "overweight"
elif BMI < 25 and BMI >= 18.5:
    status = "normal"
else:
    status = "underweight"
print(f"BMI: {BMI:.2f}")
print(f"Weight status: {status}")