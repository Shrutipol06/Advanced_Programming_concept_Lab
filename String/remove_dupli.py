s = input("Enter a string: ")

result = ""

for i in range(len(s)):
    found = False

    for j in range(i):
        if s[i] == s[j]:
            found = True

    if not found:
        result += s[i]

print(result)