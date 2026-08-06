# Initialize parallel lists for student names and grades
student_names = []
student_grades = []


def add_student(name, grade):
    """Adds a new student and their grade to the lists."""
    if name in student_names:
        print(f"Error: {name} is already in the system. Use update instead.")
        return

    student_names.append(name)
    student_grades.append(grade)
    print(f"Added {name} with a grade of {grade}.")


def update_grade(name, new_grade):
    """Updates the grade of an existing student."""
    if name in student_names:
        index = student_names.index(name)
        old_grade = student_grades[index]
        student_grades[index] = new_grade
        print(f"Updated {name}'s grade from {old_grade} to {new_grade}.")
    else:
        print(f"Error: Student '{name}' not found.")


def remove_student(name):
    """Removes a student and their grade from the system."""
    if name in student_names:
        index = student_names.index(name)
        student_names.pop(index)
        removed_grade = student_grades.pop(index)
        print(f"Removed {name} (Grade: {removed_grade}) from the system.")
    else:
        print(f"Error: Student '{name}' not found.")


def calculate_average():
    """Calculates and displays the class average grade."""
    if not student_grades:
        print("No student data available to calculate average.")
        return

    average = sum(student_grades) / len(student_grades)
    print(f"Class Average Grade: {average:.2f}")


def display_extremes():
    """Displays the highest and lowest grades in the class with student names."""
    if not student_grades:
        print("No student data available.")
        return

    max_grade = max(student_grades)
    min_grade = min(student_grades)

    # Find corresponding student names
    top_students = [
        student_names[i]
        for i, g in enumerate(student_grades)
        if g == max_grade
    ]
    bottom_students = [
        student_names[i]
        for i, g in enumerate(student_grades)
        if g == min_grade
    ]

    print(
        f"Highest Grade: {max_grade} (Student(s): {', '.join(top_students)})"
    )
    print(
        f"Lowest Grade:  {min_grade} (Student(s): {', '.join(bottom_students)})"
    )


def display_all():
    """Utility function to view the complete class roster."""
    if not student_names:
        print("The roster is currently empty.")
        return

    print("\n--- Current Class Roster ---")
    for name, grade in zip(student_names, student_grades):
        print(f"{name}: {grade}")


def main():
    """Interactive menu for managing student grades."""
    while True:
        print("\n=================================")
        print(" STUDENT GRADE MANAGEMENT SYSTEM ")
        print("=================================")
        print("1. Add Student")
        print("2. Update Student Grade")
        print("3. Remove Student")
        print("4. Calculate Class Average")
        print("5. Display Highest and Lowest Grades")
        print("6. View All Students")
        print("7. Exit")

        choice = input("\nEnter choice (1-7): ").strip()

        if choice == "1":
            name = input("Enter student name: ").strip()
            try:
                grade = float(input("Enter student grade: "))
                add_student(name, grade)
            except ValueError:
                print("Invalid input! Grade must be a number.")

        elif choice == "2":
            name = input("Enter student name to update: ").strip()
            try:
                new_grade = float(input("Enter new grade: "))
                update_grade(name, new_grade)
            except ValueError:
                print("Invalid input! Grade must be a number.")

        elif choice == "3":
            name = input("Enter student name to remove: ").strip()
            remove_student(name)

        elif choice == "4":
            calculate_average()

        elif choice == "5":
            display_extremes()

        elif choice == "6":
            display_all()

        elif choice == "7":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid option. Please enter a number from 1 to 7.")


if __name__ == "__main__":
    main()