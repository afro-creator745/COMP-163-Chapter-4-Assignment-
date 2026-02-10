#Required information
student_name = "Hakeem Cole"
current_gpa = 3.9
study_hours = 4
social_points = 45
stress_level = 40
print("Welcome", student_name + "!")
print("Current GPA:", current_gpa)
print("Study hours:", study_hours)
print("Social points:", social_points)
print("Stress level:", stress_level)  #Foundation test ran complete

#presenting the 3 course load options
print("Select Course Load\n ", "Light - Standard - Heavy")
course_load = input()
if (course_load == "Light") or (course_load == "Standard") or (course_load == "Heavy"): #this if statement here checks and confirms that the user selects a valid option.
    if course_load == "Light":
        class_attendance = input("Will you attend class today? (Y/N)")

        if class_attendance == "Y": # this is the first decision you'll make as a student in this game
            print("You attend class today")
            study_hours += 1
            stress_level -= 4
            study_choice = input("Will you study? (Y/N)")
        elif class_attendance == "N":
            print("You did not attend class today")
            study_hours -= 1
            stress_level += 4
            study_choice = input("Will you study? (Y/N)")
        else:
            print("Invalid Choice")



    if course_load == "Standard":

    if course_load == "Heavy":



else:
    print("Invalid Choice")