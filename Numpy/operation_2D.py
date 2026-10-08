import numpy as np

a = np.array([
    [10, 20],
    [30, 40]
])

b = np.array([
    [1, 2],
    [3, 4]
])

#addition
result = a + b
print("Addition:")
print(result)

#subtraction
result = a - b
print("Subtraction:")
print(result)

#Multiplication
result=a*b
print("Multiplication:")
print(result)

#Division
result=a/b
print("Division:")
print(result)

#Transpose
arr = np.array([
    [10, 20, 30],
    [40, 50, 60]
])

print("Original Array:")
print(arr)

print("Transpose:")
print(arr.T)

#exponential
arr1 = np.array([
    [1, 2],
    [3, 4]
])

result = np.exp(arr1)

print("Original Array:")
print(arr1)

print("Exponential:")
print(result)
