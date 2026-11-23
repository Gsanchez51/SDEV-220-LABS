#Geovanny Sanchez
#Module_Lab_2_Student_GPA.py
#Program made to take students first, last name and GPA
#determining if they qualify for Dean's List or Honor Roll

while True:
    last_name = input("Enter student's last name or ZZZ to quit: ")

    if last_name == "ZZZ":
        print("Process Quit.")
        break

    first_name = input("Enter student's first name: ")
    gpa = float(input("Enter student's GPA: "))

    if gpa >= 3.5:
        print(first_name, last_name, "has made the Dean's List!")

    elif gpa >= 3.25:
        print(first_name, last_name, "has made Honor Roll!")

    else:
        print(first_name, last_name, "does not qualify for either list")