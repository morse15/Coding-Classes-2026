
#check function to allow users to correct mistakes before final print
# #REMOVED because I felt it was annoying and likely unneeded
# def checkFunc(variable):
#      while True:
#         check = input(f"Is {variable} correct? \nY/N: ")
#         if check.upper() == "Y":
#             break
#         elif check.upper() == "N":
#             variable = input("Please enter the correct information: ")
#             pass
#         else:
#             print(f"Please pick 'Y' or 'N'")
#             pass
#while loop that finds the amount of courses the user has while bypassing ValueErrors
def cgpaFunc():
    #establishing the dictionary
    CGPArecords = {}

    while True:
        try:
            numCourses = int(input("How many courses do you have: "))
            ##checkFunc(numCourses)##
            if numCourses < 1:
                print ("You can not have less than 1 course")
            else:
                break
        except ValueError:
            print("Please input a whole number.\n")

    #for loop to ask for information depending on how many courses
    for course in range(numCourses):
        #COURSE NAME
        courseName = input("\nWhat is the name of your course: ")
        ##checkFunc(courseName)##
        #looks better if it just says "courseName" if only one course
        #wanted to do this in a function but couldn't figure out how to change the key and value in this way.
        if numCourses == 1:
            CGPArecords["courseName"] = courseName
        else:
            CGPArecords[f"courseName{course+1}"] = courseName

        #SCORE
        #while loop to make sure the user does not add a score above 100 or less than 0
        while True:
            #try score with an exception for ValueErrors
            try:
                score = int(input(f"What was your score for {courseName}: "))
                if score < 0:
                    print("Your score cannot be less than 0")
                elif score > 100:
                    print("Your score can not be more than 100")
                else:
                    ##checkFunc(score)##
                    #if else block for a cleaner look
                    if numCourses == 1:
                        CGPArecords["score"] = score
                    else:
                        CGPArecords[f"score{course+1}"] = score
                    break
            except ValueError:
                #should it allow a float?
                print("Please input a whole number. \n")
    
        #GRADE
        #code to determine 'grade' using 'score' and if,elif,else statements
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
        #adding grade to the dictionary
        if numCourses == 1:
            CGPArecords["grade"] = grade
        else:
            CGPArecords[f"grade{course+1}"] = grade

        #UNIT
        while True:
            try:
                numUnits = int(input(f"How many units are in {courseName}: "))
                if numUnits > 4:
                    print ("You can not have more than 4 units.")
                elif numUnits < 1:
                    print ("You can not have less than 1 unit")
                else:
                    ##checkFunc(numUnits)##
                    if numCourses == 1:
                        CGPArecords["numUnits"] = numUnits
                    else:
                        CGPArecords[f"numUnits{course+1}"] = numUnits
                    break
            except ValueError:
                #yet again should it allow a float?
                print("Please input a whole number.\n")
        
        #POINT
        #converts grade to point
        if grade == "A":
            point = 4
        elif grade == "B":
            point = 3
        elif grade == "C":
            point = 2
        elif grade == "D":
            point = 1
        elif grade == "F":
            point = 0
        numPoints = point * numUnits
        if numCourses == 1:
            CGPArecords["numPoints"] = numPoints
        else:
            CGPArecords[f"numPoints{course+1}"] = numPoints

    #PRINT
    print("---------------------------------")
    print("COURSE  SCORE  GRADE  UNITS  POINTS")
    print("---------------------------------")
    #have to use a for loop
    units = 0
    points = 0
    for num in range(numCourses):
        if numCourses == 1:
            line = (f"{CGPArecords["courseName"]}  ")
            line += (f"{CGPArecords["score"]}     ")
            line += (f"{CGPArecords["grade"]}      ")
            line += (f"{CGPArecords["numUnits"]}       ")
            line += (f"{CGPArecords["numPoints"]}")
            units = CGPArecords["numUnits"]
            points = CGPArecords["numPoints"]
            print (line)
        else:
            line = (f"{CGPArecords[f"courseName{num+1}"]}  ")
            line += (f"{CGPArecords[f"score{num+1}"]}     ")
            line += (f"{CGPArecords[f"grade{num+1}"]}      ")
            line += (f"{CGPArecords[f"numUnits{num+1}"]}       ")
            line += (f"{CGPArecords[f"numPoints{num+1}"]}")
            units += CGPArecords[f"numUnits{num+1}"]
            points += CGPArecords[f"numPoints{num+1}"]
            print (line)
    print("---------------------------------")
    print(f"Total Units: {units}")
    print(f"Total Points: {points}")
    gpa = points/units
    print(f"GPA: {gpa:.2f}")
    print("---------------------------------")
    print(CGPArecords)
cgpaFunc()