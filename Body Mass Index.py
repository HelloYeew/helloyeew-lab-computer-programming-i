"""
Please enter your weight (kg): 50.5
Please enter your height (cm): 165
Your BMI: 18.55
"""
weight = float(input("Please enter your weight (kg): "))
height = int(input("Please enter your height (cm): "))
BMI = weight/(height/100)**2
print(f"Your BMI: {BMI:.2f}")