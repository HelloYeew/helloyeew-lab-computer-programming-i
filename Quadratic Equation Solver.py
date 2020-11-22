import sys
a = float(input("1st coefficient: "))
if a==0:
    print("1st coefficient can't be zero. Program exits.")
    sys.exit()
b = float(input("2nd coefficient: "))
c = float(input("3rd coefficient: "))
d = b**2 - 4*a*c
if d>0:
    answer1 = (-b+(d**0.5))/(2*a)
    answer2 = (-b-(d**0.5))/(2*a)
    print(f"Two real roots: {answer1:.3f} and {answer2:.3f}")
if d==0:
    answer1 = -b/(2*a)
    print(f"There is one real root: {answer1:.3f}")
if d<0:
    answer_part1 = -b/(2*a)
    answer_part2 = ((-d)**0.5)/(2*a)
    if answer_part2<0:
        answer_part2 = answer_part2*-1
        print(f"Two complex roots: {answer_part1:.3f}+{answer_part2:.3f}i and {answer_part1:.3f}-{answer_part2:.3f}i")
    else :
        print(f"Two complex roots: {answer_part1:.3f}+{answer_part2:.3f}i and {answer_part1:.3f}-{answer_part2:.3f}i")
# if d<0 :
#     answer_part1 = -b / (2 * a)
#     answer_part2 = ((-d)**0.5)/(2*a)
#     print(f"Two complex roots: {answer_part1:.3f}+{answer_part2:.3f}i and {answer_part1:.3f}-{answer_part2:.3f}i")
