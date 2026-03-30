from coursesCSV import courses as c

names = []
scores = []
grades = []
unit = []
points = []
point = []
#for loop to ask for information depending on how many courses
for x in c:
    #COURSE NAME
    names.append(x["name"])

    #SCORE
    #while loop to make sure the user does not add a score above 100 or less than 0
    scores.append(x["score"])

    #UNIT
    unit.append(x["unit"])
#GRADE
#code to determine 'grade' using 'score' and if,elif,else statements
#scores = [1,2,4,5,3,6,7,8,9,0]
#if scores in the course place > 69:
#   grade = "A"
#   grades.append(grade)
for score in scores:
    if score > 69:
        grade = "A"
    elif score > 59:
        grade = "B"
    elif score > 49:
        grade = "C"
    elif score > 44:
        grade = "D"
    else:
        grade = "F"
    grades.append(grade)

    #POINT
    #converts grade to point
    if grade == "A":
        point_ = 4
    elif grade == "B":
        point_ = 3
    elif grade == "C":
        point_ = 2
    elif grade == "D":
        point_ = 1
    elif grade == "F":
        point_ = 0  
    point.append(point_)

#point * unit
#access unit using a for loop and point in the loop also
for u in range(len(unit)):
    print(unit[u])
    points.append(point[u] * unit[u])

#PRINT
line = ""
print("---------------------------------")
print("COURSE  SCORE  GRADE  UNITS  POINTS")
print("---------------------------------")
for x in range(len(names)):
    if x == (len(names) - 1):
        line += (f"{names[x]}  ")
        line += (f"{scores[x]}     ")
        line += (f"{grades[x]}      ")
        line += (f"{unit[x]}      ")
        line += (f"{points[x]}")
    else:
        line += (f"{names[x]}  ")
        line += (f"{scores[x]}     ")
        line += (f"{grades[x]}      ")
        line += (f"{unit[x]}      ")
        line += (f"{points[x]}\n")
print (line)
print("---------------------------------")
totalUnits = sum(unit)
totalPoints = sum(points)
print(f"Total Units: {totalUnits}")
print(f"Total Points: {totalPoints}")
gpa = totalPoints/totalUnits
print(f"GPA: {gpa:.2f}")
print("---------------------------------")
