# Program to find sum of odd numbers up to n

n = int(input("Enter n: "))

i = 1
total = 0

while i <= n:
    if i % 2 != 0:
        total += i
    i += 1

print("Sum of odd numbers =", total)