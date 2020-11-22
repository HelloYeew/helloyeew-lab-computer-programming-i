# What is the year (AD)? 1800
# AD 1800 is not a leap year
import sys
year = int(input("What is the year (AD)? "))
if year<1:
    print("Invalid input: input year must be a positive integer")
    sys.exit()
if year < 1752:
    if year % 4 == 0:
        print(f"AD {year} is a leap year")
    else:
        print(f"AD {year} is not a leap year")
else:
    if year % 4 != 0:
        print(f"AD {year} is not a leap year")
    elif year % 100 != 0:
        print(f"AD {year} is a leap year")
    elif year % 400 != 0:
        print(f"AD {year} is not a leap year")
    else:
        print(f"AD {year} is a leap year")