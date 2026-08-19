s = input("Enter message: ")
shift = int(input("Enter shift: "))

result = ""

for ch in s:
    if ch >= 'a' and ch <= 'z':
        new = ord(ch) + shift

        if new > ord('z'):
            new = new - 26

        result += chr(new)

    elif ch >= 'A' and ch <= 'Z':
        new = ord(ch) + shift

        if new > ord('Z'):
            new = new - 26

        result += chr(new)

    else:
        result += ch

print("Encrypted:", result)