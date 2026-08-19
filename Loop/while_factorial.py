# Program to find factorial of a given number

n = int(input("Enter a number: "))

i = 1
fact = 1

while i <= n:
    fact = fact * i
    i += 1

print("Factorial =", fact)