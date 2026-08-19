# Program to check whether a number is prime or not

n = int(input("Enter a number: "))

i = 2
prime = True

if n < 2:
    prime = False

while i < n:
    if n % i == 0:
        prime = False
        break
    i += 1

if prime:
    print("Prime number")
else:
    print("Not a prime number")