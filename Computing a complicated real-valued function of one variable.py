num = float(input("Enter a real number: "))
if num<=15:
    answer = (2*num)+10
elif num>15 and num<=35:
    answer = 3*(num**2)
else:
    answer = (2*(num**3))-5
print(f"f({num:.3f}) = {answer:.3f}")