email = input("Enter email: ")

at_count = 0
dot_count = 0
at_position = -1
dot_position = -1

for i in range(len(email)):
    if email[i] == '@':
        at_count += 1
        at_position = i

    if email[i] == '.':
        dot_count += 1
        dot_position = i

if at_count == 1 and dot_count >= 1 and at_position > 0 and dot_position > at_position + 1 and dot_position < len(email) - 1:
    print("Valid Email")
else:
    print("Invalid Email")