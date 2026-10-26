import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Student Registration Form")
root.geometry("400x500")

# Heading
tk.Label(root, text="Student Registration Form",
         font=("Arial", 16, "bold")).pack(pady=10)

# Name
tk.Label(root, text="Enter Name:").pack()
name_entry = tk.Entry(root)
name_entry.pack()

# Age
tk.Label(root, text="Enter Age:").pack()
age_entry = tk.Entry(root)
age_entry.pack()

# Gender
tk.Label(root, text="Select Gender:").pack()
gender = tk.StringVar(value="Male")

tk.Radiobutton(root, text="Male",
               variable=gender, value="Male").pack()
tk.Radiobutton(root, text="Female",
               variable=gender, value="Female").pack()

# Course
tk.Label(root, text="Select Course:").pack()
course = tk.StringVar(value="Python")

courses = ["Python", "Java", "C++", "Data Science"]
tk.OptionMenu(root, course, *courses).pack()

# Hobbies
tk.Label(root, text="Select Hobbies:").pack()
hobby1 = tk.IntVar()
hobby2 = tk.IntVar()

tk.Checkbutton(root, text="Reading",
               variable=hobby1).pack()
tk.Checkbutton(root, text="Sports",
               variable=hobby2).pack()

# Submit Function
def submit():
    name = name_entry.get()
    age = age_entry.get()

    if name == "" or age == "":
        messagebox.showwarning("Warning", "Please fill all fields")
    else:
        messagebox.showinfo(
            "Success",
            f"Name: {name}\nAge: {age}\n"
            f"Gender: {gender.get()}\n"
            f"Course: {course.get()}"
        )

# Buttons
tk.Button(root, text="Submit",
          command=submit).pack(pady=10)

tk.Button(root, text="Clear",
          command=lambda: [name_entry.delete(0, tk.END),
                           age_entry.delete(0, tk.END)]).pack()

root.mainloop()