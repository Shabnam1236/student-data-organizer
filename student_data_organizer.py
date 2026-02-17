print("Welcome to the Student Data Organizer!")
students = []

while True:
    # Display menu
    print("\nSelect an option:")
    print("1. Add student")
    print("2. Display all students")
    print("3. Update student information")
    print("4. Delete student")
    print("5. Display subjects offered")
    print("6. Exit")

    # Take user input
    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        # Add student
        sid = input("Enter student ID:")
        name = input("Enter student name: ")
        age = input("Enter student age: ")
        grade = input("Enter student grade:")
        dob = input("Enter student date of birth:")
        subjects = input("Enter student subjects:")
        students.append({"ID":sid, "Name": name, "Age": age,"grade": grade, "dob":dob,"subjects":subjects})
        print("Student added successfully!")

    elif choice == "2":
        # Display all students
        if not students:
            print("No students found.")
        else:
            print("\nList of Students:")
            for student in students:
                  # Check keys exist before printing
                sid = student.get("ID", "786")
                sname = student.get("Name", "N/A")
                sage = student.get("Age", "N/A")
                sgrade = student.get("Grade","A")
                ssubjects = student.get("Subjects","N/A")
                print(f"ID: {sid}, Name: {sname}, Age: {sage}, Grade:{sgrade},Subjects:{subjects},:")
                break

    elif choice == "3":
        # Update student
        sid = input("Enter student ID to update: ")
        found = False
        for student in students:
            if student["ID"]==sid:
                student["Name"] = input("Enter new name: ")
                student["Age"] = input("Enter new age: ")
                print("Student information updated!")
                found = True
                break
        if not found:
            print("Student not found.")

    elif choice == "4":
        # Delete student
        sid = input("Enter student ID to delete: ")
        found = False
        for student in students:
            if student["ID"] == sid:
                students.remove(student)
                print("Student deleted!")
                found = True
                break
        if not found:
            print("Student not found.")

    elif choice == "5":
        # Display subjects offered
        subjects = ["Math", "Science", "English", "History", "Computer"]
        print("Subjects Offered:", ", ".join(subjects))

    elif choice == "6":
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice! Please enter a number between 1 and 6.")
