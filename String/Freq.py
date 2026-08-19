s = input("Enter a string: ")

max_count = 0
max_char = ""

for i in range(len(s)):
    count = 0

    for j in range(len(s)):
        if s[i] == s[j]:
            count += 1

    if count > max_count:
        max_count = count
        max_char = s[i]

print("Most frequent:", max_char)