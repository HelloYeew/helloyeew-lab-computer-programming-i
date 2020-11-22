# Enter initial amount in Baht: 100
# Enter interest rate in percent: 3
# Total amount after 1 year is 103.00 Baht.
# Total amount after 5 years is 115.93 Baht.
# Total amount after 10 years is 134.39 Baht.
# Total amount after 20 years is 180.61 Baht.
baht = int(input("Enter initial amount in Baht: "))
interest = int(input("Enter interest rate in percent: "))
baht1 = baht*(1+(interest/100))**1
baht5 = baht*(1+(interest/100))**5
baht10 = baht*(1+(interest/100))**10
baht20 = baht*(1+(interest/100))**20
print(f"Total amount after 1 year is {baht1:.2f} Baht.")
print(f"Total amount after 5 years is {baht5:.2f} Baht.")
print(f"Total amount after 10 years is {baht10:.2f} Baht.")
print(f"Total amount after 20 years is {baht20:.2f} Baht.")
