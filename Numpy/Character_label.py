import numpy as np

arr = np.array([
    ('A', 10),
    ('B', 20),
    ('C', 30)
], dtype=[('Label', 'U1'), ('Value', 'i4')])

print("Array with Character Labels:")
print(arr)