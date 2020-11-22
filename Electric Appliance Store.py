# Enter the number of TVs: 1
# Enter the number of DVD players: 0
# Enter the number of audio systems: 1
# The total amount is 9000.00 baht.
# Please pay 9000.00 baht. Thank you very much.
# The store offers 20% discount to the customer who purchases at least 20000 bahts.
tv = int(input("Enter the number of TVs: "))
dvd = int(input("Enter the number of DVD players: "))
audio = int(input("Enter the number of audio systems: "))
total = (tv*6000)+(dvd*1500)+(audio*3000)
if total>20000:
    print(f"The total amount is {total:.2f} baht.")
    discount=total*0.2
    print(f"You got a discount of {discount:.2f} baht.")
    total = total-discount
    print(f"Please pay {total:.2f} baht. Thank you very much.")
else :
    print(f"The total amount is {total:.2f} baht.")
    print(f"Please pay {total:.2f} baht. Thank you very much.")