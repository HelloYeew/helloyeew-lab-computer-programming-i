studentscore = []
while True:
    score = str(input("Input student score (or just ENTER to finish): "))
    if score == "":
        break
    else:
        studentscore.append(score)
for i in range (len(studentscore)):
    studentscore[i] = int(studentscore[i])
for m in range (len(studentscore)):
    print(f"Student #{m+1} score: {studentscore[m]}")
avg = sum(studentscore) / len(studentscore)
print(f"Average score is {avg:.2f}")
print(f"Minimum score is {min(studentscore)}")
print(f"Maximum score is {max(studentscore)}")