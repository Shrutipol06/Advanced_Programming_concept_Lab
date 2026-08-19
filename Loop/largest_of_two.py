# Program to find the largest of two numbers

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if a > b:
    print("Largest number =", a)
elif b > a:
    print("Largest number =", b)
else:
    print("Both numbers are equal.")