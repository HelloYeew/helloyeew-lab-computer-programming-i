studentscore = []
while True:
    score = str(input("Input student score (or just ENTER to finish): "))
    if score == "":
        break
    else:
        studentscore.append(score)
studentscore.sort(reverse=True)
for i in range(len(studentscore)):
    print(f"Rank #{i+1}: {studentscore[i]}")