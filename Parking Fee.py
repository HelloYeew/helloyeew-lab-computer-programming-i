# Enter parking time in minutes: 30
# Parking fee is 25 baht.
import math
time = int(input("Enter parking time in minutes: "))
fee = (math.ceil(time/60))*25
print(f"Parking fee is {fee} baht.")
