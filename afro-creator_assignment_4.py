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
                social_points -= 10

            elif class_attendance == "N":
                print("You did not attend class today")
                study_hours -= 3
                stress_level += 10
                current_gpa -= 0.8
                social_points += 10
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
            social_points += 10
        if "Student Center" in user_study_location:
            study_hours = study_hours + user_study_location.count("Student Center") * 1
            stress_level -= 1
            social_points += 15
        if "Dorm study rooms" in user_study_location:
            study_hours = study_hours + user_study_location.count("Dorm study rooms") * 2
            stress_level -= 5
            social_points += 2
    elif study_choice == "N":
        study_hours -= 5
        social_points += 20
    else:
        print("Invalid choice")
 #Step 4, here is where all the states will have an` effect on your results
    print("\nStats Reports") #the start of the end game stat report
    print(student_name)

    mood = "neutral" #addeds in a mood factor that is based on you stress level which in turn effects how many study hours you would need to pass
    if stress_level <= 26:
        mood = "confident"
    elif stress_level <= 40:
        mood = "moderate"
    elif stress_level <= 50:
        mood = "overwhelmed"

    easy = "confident"
    medium = "moderate"
    hard = "overwhelmed"
#The if statements that determine whether you pass or not and not passing effects your gpa
    if mood is easy:
        if (course_load == "Heavy") and (study_hours >= 10):
           print("You passed your test")
        elif (course_load == "Standard") and (study_hours >= 6):
            print("You passed your test")
        elif (course_load == "Light") and (study_hours >= 4):
            print("You passed your test")
        else:
            print("You Failed your test")
            current_gpa -=0.5

    if mood is medium:
        if (course_load == "Heavy") and (study_hours >= 12):
           print("You passed your test")
        elif (course_load == "Standard") and (study_hours >= 8):
            print("You passed your test")
        elif (course_load == "Light") and (study_hours >= 5):
            print("You passed your test")
        else:
            print("You Failed your test")
            current_gpa -=0.5

    if mood is hard:
        if (course_load == "Heavy") and (study_hours >= 14):
           print("You passed your test")
        elif (course_load == "Standard") and (study_hours >= 9):
            print("You passed your test")
        elif (course_load == "Light") and (study_hours >= 6):
            print("You passed your test")
        else:
            print("You Failed your test")
            current_gpa -=0.5

#The social point you collected will effect whether you were considered active or not on campus
    if social_points < 50:
        print("School Involvement: Barely Involved")
    elif social_points < 58:
        print("School Involvement: Average Involvement")
    else:
        print("School Involvement: Highly Involved")

#Display the stats

    print("Stress Level:",stress_level)
    print("Current Mood:",mood)
    print("Study Hours:", study_hours)
    print("Social Points:", social_points)
    print("Current GPA:" ,current_gpa)


else:
    print("Invalid Choice")




