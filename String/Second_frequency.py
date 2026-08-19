s = input("Enter a string: ")

first = 0
second = 0
first_char = ""
second_char = ""

for i in range(len(s)):
    count = 0

    for j in range(len(s)):
        if s[i] == s[j]:
            count += 1

    if count > first:
        second = first
        second_char = first_char
        first = count
        first_char = s[i]
    elif count > second and count != first:
        second = count
        second_char = s[i]

print("Second most frequent:", second_char)