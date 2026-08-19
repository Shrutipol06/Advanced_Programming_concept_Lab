n = int(input("Enter number of rows: "))

for i in range(n):
    for j in range(3):
        print(chr(65 + j), end="")
    print()


n = int(input("Enter n: "))

for i in range(1, n + 1):
    for j in range(i):
        print(chr(65 + j), end="")
    print()


n = int(input("Enter n: "))

for i in range(n, 0, -1):
    for j in range(i):
        print(chr(65 + j), end="")
    print()


n = int(input("Enter n: "))

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()


n = int(input("Enter n: "))

for i in range(1, n + 1):
    for j in range(i):
        print(i, end="")
    print()

