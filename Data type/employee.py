# Employees in two projects

project1 = {"Rahul", "Priya", "Amit", "Sneha"}
project2 = {"Amit", "Sneha", "Rohan", "Neha"}

# Employees working on both projects
both = project1 & project2

# Employees working only on Project 1
only_project1 = project1 - project2

# Employees working only on Project 2
only_project2 = project2 - project1

# Total unique employees
all_employees = project1 | project2

print("Employees in Project 1:", project1)
print("Employees in Project 2:", project2)

print("\nEmployees working on both projects:", both)

print("Employees only in Project 1:", only_project1)

print("Employees only in Project 2:", only_project2)

print("Total unique employees:", all_employees)