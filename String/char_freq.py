s = input("Enter a string: ")

for i in range(len(s)):
    count = 0
    already = False

    for k in range(i):
        if s[i] == s[k]:
            already = True

    if not already:
        for j in range(len(s)):
            if s[i] == s[j]:
                count += 1

        print(s[i], ":", count)