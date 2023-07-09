def average_grade_dictionary(grade_list):
    d1 = dict() # Create a blank dictionary
    for i in grade_list:
        total = 0
        name = input("Enter name of student:") # Assign name of student to name variable
        for j in i:
            if j == "O": # Create grade_points from grade
                grade_points = 10
            elif j == "E":
                grade_points = 9
            elif j == "A":
                grade_points = 8
            elif j == "B":
                grade_points = 7
            elif j == "C":
                grade_points = 6
            elif j == "D":
                grade_points = 5
            elif j == "F":
                grade_points = 0
            else:
                grade_points = 0
            total += grade_points
        grade_point_average = total / len(i) # Find grade_point_average
        if grade_point_average == 10: # Create average_grade from grade_point_average
            average_grade = "O"
        elif 9 <= grade_point_average < 10:
            average_grade = "E"
        elif 8 <= grade_point_average < 9:
            average_grade = "A"
        elif 7 <= grade_point_average < 8:
            average_grade = "B"
        elif 6 <= grade_point_average < 7:
            average_grade = "C"
        elif 5 <= grade_point_average < 6:
            average_grade = "D"
        elif 0 <= grade_point_average < 5:
            average_grade = "F"
        d1[name] = average_grade
    print("The dictionary where student names are keys and corresponding average grades are the values is:")
    return d1 # Return required dictionary
grades_in_list=[["O","A","B","E"],["F","D","F","C"],["A","O","A","B"]]
print(average_grade_dictionary(grades_in_list))