student = {
    "name": "Shruti",
    "age": 20,
    "branch": "CSE",
    "marks": 85
}

print("\nDICTIONARY:", student)

# 1. get() - gets value
print("1. get:", student.get("name"))

# 2. keys() - gets all keys
print("2. keys:", student.keys())

# 3. values() - gets all values
print("3. values:", student.values())

# 4. items() - gets key-value pairs
print("4. items:", student.items())

# 5. update() - updates dictionary
student.update({"marks": 90})
print("5. update:", student)

# 6. pop() - removes a key
student.pop("age")
print("6. pop:", student)

# 7. popitem() - removes last key-value pair
student.popitem()
print("7. popitem:", student)

# 8. setdefault() - adds key if it does not exist
student.setdefault("city", "Kolhapur")
print("8. setdefault:", student)

# 9. copy() - creates a copy
student2 = student.copy()
print("9. copy:", student2)

# 10. clear() - removes all elements
student2.clear()
print("10. clear:", student2)