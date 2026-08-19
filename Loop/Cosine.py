x = float(input("Enter x in radians: "))
n = int(input("Enter number of terms: "))

sum = 0
fact = 1

for i in range(n):
    power = 2 * i

    if i > 0:
        fact = fact * (2 * i - 1) * (2 * i)

    term = (x ** power) / fact

    if i % 2 == 0:
        sum = sum + term
    else:
        sum = sum - term

print("Cosine =", sum)