names = []
grades = []


def add_student():
    name = input("Enter student name: ")
    grade = float(input("Enter grade: "))

    names.append(name)
    grades.append(grade)

    print("Student added successfully.")


def update_grade():
    name = input("Enter student name: ")

    found = False

    for i in range(len(names)):
        if names[i] == name:
            grades[i] = float(input("Enter new grade: "))
            found = True
            print("Grade updated successfully.")
            break

    if not found:
        print("Student not found.")


def remove_student():
    name = input("Enter student name: ")

    found = False

    for i in range(len(names)):
        if names[i] == name:
            names.pop(i)
            grades.pop(i)
            found = True
            print("Student removed successfully.")
            break

    if not found:
        print("Student not found.")


def calculate_average():
    if len(grades) == 0:
        print("No students available.")
        return

    total = 0

    for grade in grades:
        total += grade

    average = total / len(grades)

    print("Average grade:", average)


def highest_lowest():
    if len(grades) == 0:
        print("No students available.")
        return

    highest = grades[0]
    lowest = grades[0]

    for grade in grades:
        if grade > highest:
            highest = grade

        if grade < lowest:
            lowest = grade

    print("Highest grade:", highest)
    print("Lowest grade:", lowest)


while True:
    print("\n--- Student Grade Management System ---")
    print("1. Add Student")
    print("2. Update Grade")
    print("3. Remove Student")
    print("4. Calculate Average")
    print("5. Display Highest and Lowest")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        update_grade()

    elif choice == "3":
        remove_student()

    elif choice == "4":
        calculate_average()

    elif choice == "5":
        highest_lowest()

    elif choice == "6":
        print("Program ended.")
        break

    else:
        print("Invalid choice.")