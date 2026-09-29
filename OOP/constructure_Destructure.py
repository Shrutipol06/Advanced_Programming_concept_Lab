class Student:
    def __init__(self):
        print("Constructor is called")

    def __del__(self):
        print("Destructor is called")


s = Student()
print("Student object is created")