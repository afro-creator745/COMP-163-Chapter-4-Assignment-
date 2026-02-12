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

#Step 2: Course Planning Decision
if (course_load == "Light") or (course_load == "Standard") or (course_load == "Heavy"): #this if statement here checks and confirms that the user selects a valid option.

#the choice question and state boost based on light course load
    if course_load == "Light":
        if current_gpa >= 2.5:
            class_attendance = input("Will you attend class today? (Y/N)")
            if class_attendance == "Y": # this is the first decision you'll make as a student in this game
                print("You attend class today")
                study_hours += 1
                stress_level -= 4
                current_gpa += 0.1

            elif class_attendance == "N":
                print("You did not attend class today")
                study_hours -= 1
                stress_level += 4
                current_gpa -= 0.3
        else:
            print("Not qualified")

# the choice question and state boost based on standard course load
    if course_load == "Standard":
        if current_gpa >= 3.0:
            class_attendance = input("Will you attend class today? (Y/N)")

            if class_attendance == "Y": # this is the first decision you'll make as a student in this game
                print("You attend class today")
                study_hours += 3
                stress_level -= 6
                current_gpa += 0.3

            elif class_attendance == "N":
                print("You did not attend class today")
                study_hours -= 3
                stress_level += 6
                current_gpa -= 0.5
        else:
            print("Not qualified")

# the choice question and state boost based on heavy course load
    if course_load == "Heavy":
        if current_gpa >= 3.7:
            class_attendance = input("Will you attend class today? (Y/N)")

            if class_attendance == "Y": # this is the first decision you'll make as a student in this game
                print("You attend class today")
                study_hours += 4
                stress_level -= 8
                current_gpa += 0.6

            elif class_attendance == "N":
                print("You did not attend class today")
                study_hours -= 3
                stress_level += 10
                current_gpa -= 0.8
        else:
            print("Not qualified")



    study_choice = input("Will you study today? (Y/N)") #This is the next decision you'll make. Deciding whether you'll study or not

    if study_choice == "Y":
        print("Study location options: Library, Student Center, Dorm study rooms")
#here you're choosing where you'll study which will ultimately affect your study hours and stress levels
        study_location = ["Library", "Student Center", "Dorm study rooms"]
        where_did_you_study1 = input("Where did you study? ")
        where_did_you_study2 = input("Where did you study? ")
        where_did_you_study3 = input("Where did you study? ")
        user_study_location = [where_did_you_study1, where_did_you_study2, where_did_you_study3]

        if "Library" in user_study_location: #checks the locations you selected and adjusts your stats accordingly
            study_hours = study_hours + user_study_location.count("Library") * 3
            stress_level -= 10
        if "Student Center" in user_study_location:
            study_hours = study_hours + user_study_location.count("Student Center") * 1
            stress_level -= 1
        if "Dorm study rooms" in user_study_location:
            study_hours = study_hours + user_study_location.count("Dorm study rooms") * 2
            stress_level -= 5
    elif study_choice == "N":
        study_hours -= 5
    else:
        print("Invalid choice")
else:
    print("Invalid Choice")
print(study_hours)
