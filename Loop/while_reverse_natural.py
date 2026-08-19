# Program to print natural numbers up to n in reverse order

n = int(input("Enter n: "))

i = n

while i >= 1:
    print(i, end=" ")
    i -= 1