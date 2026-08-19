s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if len(s1) != len(s2):
    print("No")
else:
    found = False

    for i in range(len(s1)):
        match = True

        for j in range(len(s1)):
            if s1[(i + j) % len(s1)] != s2[j]:
                match = False
                break

        if match:
            found = True
            break

    if found:
        print("Yes")
    else:
        print("No")