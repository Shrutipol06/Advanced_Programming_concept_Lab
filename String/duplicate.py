text=input("enter a string: ")
duplicates= []
for char in text:
    if text.count(char)>1 and char not in duplicates:
        duplicates.append(char)
if duplicates:
    print("duplicate characters:",", ".join(duplicates))
else:
    print("no duplicate character found.")
