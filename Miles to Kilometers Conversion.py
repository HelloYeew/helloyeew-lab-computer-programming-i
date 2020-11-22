# Enter the distance in miles: 2.5
# The distance is 4.02 kilometers.
KILOMETERS_PER_MILE = 1.609

def miles_to_kilometers(miles) :
    return miles*KILOMETERS_PER_MILE

miles = float(input("Enter the distance in miles: "))
print(f"The distance is {miles_to_kilometers(miles):.2f} kilometers.")