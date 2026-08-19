# Program to find sum of natural numbers up to n

n = int(input("Enter n: "))

i = 1
total = 0

while i <= n:
    total += i
    i += 1

print("Sum =", total)