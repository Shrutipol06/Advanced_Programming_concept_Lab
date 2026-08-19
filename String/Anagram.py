s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if len(s1) != len(s2):
    print("Not Anagram")
else:
    matched = True

    for i in range(len(s1)):
        count1 = 0
        count2 = 0

        for j in range(len(s1)):
            if s1[i] == s1[j]:
                count1 += 1

            if s1[i] == s2[j]:
                count2 += 1

        if count1 != count2:
            matched = False
            break

    if matched:
        print("Anagram")
    else:
        print("Not Anagram")