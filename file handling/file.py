# File Handling in Python

# 1. w - Write mode
with open("student.txt", "w") as file:
    file.write("Hello Python\n")
    file.write("This is my file.")


# 2. r - Read mode
with open("student.txt", "r") as file:
    data = file.read()
    print("Read Mode:")
    print(data)


# 3. a - Append mode
with open("student.txt", "a") as file:
    file.write("\nThis line is added using append mode.")


# 4. r+ - Read and Write mode
with open("student.txt", "r+") as file:
    data = file.read()
    print("\nr+ Mode:")
    print(data)

    file.write("\nNew data added using r+.")


# 5. w+ - Write and Read mode
with open("newfile.txt", "w+") as file:
    file.write("This is w+ mode.")

    # Move pointer to beginning
    file.seek(0)

    data = file.read()
    print("\nw+ Mode:")
    print(data)


# 6. a+ - Append and Read mode
with open("student.txt", "a+") as file:
    file.write("\nThis is added using a+ mode.")

    # Move pointer to beginning
    file.seek(0)

    data = file.read()
    print("\na+ Mode:")
    print(data)


# 7. x - Create mode
# Creates a new file
try:
    with open("newstudent.txt", "x") as file:
        file.write("This file is created using x mode.")
        print("\nx Mode:")
        print("File created successfully.")
except FileExistsError:
    print("\nFile already exists.")


# 8. wb - Write Binary mode
with open("binary.txt", "wb") as file:
    file.write(b"Hello Python")


# 9. rb - Read Binary mode
with open("binary.txt", "rb") as file:
    data = file.read()
    print("\nrb Mode:")
    print(data)


# 10. ab - Append Binary mode
with open("binary.txt", "ab") as file:
    file.write(b" - New Data")

print("\nAll file modes completed.")