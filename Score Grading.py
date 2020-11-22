studentscore = []
while True:
    score = str(input("Input student score (or just ENTER to finish): "))
    if score == "":
        break
    else:
        studentscore.append(score)
for i in range (len(studentscore)):
    studentscore[i] = int(studentscore[i])
avg = sum(studentscore) / len(studentscore)
sum_studentlist = []
for i in range(len(studentscore)):
    cal = (studentscore[i]-avg)**2
    sum_studentlist.append(cal)
sum_sd = sum(sum_studentlist)
SD = (sum_sd/(len(studentscore)-1))**0.5
print(f"Average score is {avg:.2f}")
print(f"Standard deviation is {SD:.2f}")
for i in range(len(studentscore)):
    if studentscore[i] >= avg+(1.5*SD):
        print(f"Student #{i+1} score: {studentscore[i]} grade: A")
    elif studentscore[i] < avg+(1.5*SD) and avg+SD <= studentscore[i]:
        print(f"Student #{i + 1} score: {studentscore[i]} grade: B+")
    elif studentscore[i] < avg+SD and avg+(0.5*SD) <= studentscore[i]:
        print(f"Student #{i + 1} score: {studentscore[i]} grade: B")
    elif studentscore[i] < avg+(0.5*SD) and avg <= studentscore[i]:
        print(f"Student #{i + 1} score: {studentscore[i]} grade: C+")
    elif studentscore[i] < avg and avg-(0.5*SD) <= studentscore[i]:
        print(f"Student #{i + 1} score: {studentscore[i]} grade: C")
    elif studentscore[i] < avg-(0.5*SD) and avg-SD <= studentscore[i]:
        print(f"Student #{i + 1} score: {studentscore[i]} grade: D+")
    elif studentscore[i] < avg-SD and avg-(1.5*SD) <= studentscore[i]:
        print(f"Student #{i + 1} score: {studentscore[i]} grade: D")
    else:
        print(f"Student #{i + 1} score: {studentscore[i]} grade: F")
