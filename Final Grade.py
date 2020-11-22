# What is the percentage for homework? 100
# What is the percentage for midterm? 60
# What is the percentage for final? 72
# Your total score is 73.40
# You receive the grade B

homework = int(input("What is the percentage for homework? "))
midterm = int(input("What is the percentage for midterm? "))
final = int(input("What is the percentage for final? "))
homework_weight = homework*0.2
midterm_weight = midterm*0.35
final_weight = final*0.45
total_score = homework_weight+midterm_weight+final_weight
if total_score>=80:
    grade = "A"
elif total_score>=75 and total_score<80:
    grade = "B+"
elif total_score>=70 and total_score<75:
    grade = "B"
elif total_score>=65 and total_score<70:
    grade = "C+"
elif total_score>=60 and total_score<65:
    grade = "C"
elif total_score>=55 and total_score<60:
    grade = "D+"
elif total_score>=55 and total_score<60:
    grade = "D"
elif total_score==50:
    grade = "D"
elif total_score<50:
    grade = "F"
print(f"Your total score is {total_score:.2f}")
print(f"You receive the grade {grade}")
