#simple lambda function
square = lambda x: x * x

print(square(5))

#lambda function with two arguments
add = lambda a, b: a + b

print(add(10, 20))

#largest number
largest = lambda a, b: a if a > b else b

print(largest(10, 20))

#Even or odd
check = lambda n: "Even" if n % 2 == 0 else "Odd"

print(check(10))
print(check(7))

#cube of number
cube = lambda x: x ** 3

print(cube(4))

#lambda with map
numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x * x, numbers))

print(squares)

#lambda with filter
numbers = [1, 2, 3, 4, 5, 6]

even = list(filter(lambda x: x % 2 == 0, numbers))

print(even)

#lambda with sorted
students = [("Amit", 80), ("Rahul", 60), ("Sneha", 90)]

students.sort(key=lambda x: x[1])

print(students)

