#Simple Function
def greet():
    print("Hello, Welcome to Python!")

greet()

#function with parameters
def add(a, b):
    print("Sum =", a + b)
add(10, 20)

#function with return value
def add(a, b):
    return a + b

result = add(10, 20)
print("Sum =", result)

#funtion to find even or odd
def check_even_odd(n):
    if n % 2 == 0:
        return "Even"
    else:
        return "Odd"

n = int(input("Enter a number: "))
print(check_even_odd(n))

#function to find largest of two numbers
def largest(a, b):
    if a > b:
        return a
    else:
        return b

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Largest =", largest(a, b))

#function to find factorial of a number
def factorial(n):
    fact = 1

    for i in range(1, n + 1):
        fact = fact * i

    return fact

n = int(input("Enter a number: "))
print("Factorial =", factorial(n))

#function to check prime number
def is_prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True

n = int(input("Enter a number: "))

if is_prime(n):
    print("Prime number")
else:
    print("Not a prime number")

#function to find sum of list
def list_sum(numbers):
    total = 0

    for n in numbers:
        total = total + n

    return total

numbers = [10, 20, 30, 40, 50]

print("Sum =", list_sum(numbers))

#function  with default arguments
def greet(name="Student"):
    print("Hello", name)

greet()
greet("Shruti")

#function with reverse string
def reverse_string(s):
    return s[::-1]

text = input("Enter a string: ")

print("Reverse =", reverse_string(text))