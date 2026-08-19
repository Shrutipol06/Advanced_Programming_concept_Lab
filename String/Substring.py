s = input("Enter main string: ")
sub = input("Enter substring: ")

found = False

for i in range(len(s) - len(sub) + 1):
    match = True

    for j in range(len(sub)):
        if s[i + j] != sub[j]:
            match = False
            break

    if match:
        found = True
        break

if found:
    print("Substring exists")
else:
    print("Substring does not exist")