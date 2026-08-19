# Writing data into a file
with open("student.txt", "w") as file:
    file.write("Hello, my name is Shruti.\n")
    file.write("I am learning Computer Science.\n")
    file.write("Computer Science is easy to learn and interesting to study .")

# Reading the complete file
with open("student.txt", "r") as file:
    data = file.read()
    print("Complete File:")
    print(data)

# Reading only one line
with open("student.txt", "r") as file:
    line = file.readline()
    print("First Line:")
    print(line)

# Reading all lines as a list
with open("student.txt", "r") as file:
    lines = file.readlines()
    print("All Lines:")
    print(lines)

# Appending data to the file
with open("student.txt", "a") as file:
    file.write("\nI am practicing file handling.")


# Using seek() and tell()
with open("student.txt", "r") as file:

    
    print("Current position:", file.tell())

    # Read first 5 characters
    data = file.read(5)
    print("First 5 characters:", data)

    print("Current position:", file.tell())

    
    file.seek(0)

    print("Position after seek:", file.tell())

    # Read the file again
    data = file.read()
    print("File after seek:")
    print(data)


# Checking if file is closed
with open("student.txt", "r") as file:
    print("File is closed:", file.closed)

print("File is closed after with block:", file.closed)