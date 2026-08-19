# Attendance dictionary

attendance = {
    "Monday": {"Rahul", "Priya", "Amit", "Sneha"},
    "Tuesday": {"Rahul", "Priya", "Amit"},
    "Wednesday": {"Rahul", "Priya", "Sneha"},
    "Thursday": {"Rahul", "Priya", "Amit", "Sneha"},
    "Friday": {"Rahul", "Priya"}
}


# Students who attended all classes
all_students = attendance["Monday"]

for day in attendance:
    all_students = all_students & attendance[day]


# Find students who attended only one class
student_count = {}

for day in attendance:
    for student in attendance[day]:

        if student in student_count:
            student_count[student] += 1
        else:
            student_count[student] = 1


only_one = set()

for student in student_count:
    if student_count[student] == 1:
        only_one.add(student)


# Find total unique students
all_unique_students = set()

for day in attendance:
    all_unique_students = all_unique_students | attendance[day]


# Display results
print("Students who attended all classes:")
print(all_students)

print("\nStudents who attended only one class:")
print(only_one)

print("\nTotal unique students:")
print(len(all_unique_students))