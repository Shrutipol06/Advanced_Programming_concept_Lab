password = input("Enter password: ")

upper = False
lower = False
digit = False
special = False

for ch in password:
    if ch >= 'A' and ch <= 'Z':
        upper = True
    elif ch >= 'a' and ch <= 'z':
        lower = True
    elif ch >= '0' and ch <= '9':
        digit = True
    else:
        special = True

if len(password) >= 8 and upper and lower and digit and special:
    print("Valid Password")
else:
    print("Invalid Password")