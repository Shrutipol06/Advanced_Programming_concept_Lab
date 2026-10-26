import pandas as pd

data = {
    'Name': ['Amit', 'Sneha', 'Rahul', 'Priya', 'Rohan', 'Neha'],
    'Age': [20, 21, 19, 22, 20, 21],
    'Marks': [85, 90, 78, 95, 88, 92]
}

df = pd.DataFrame(data)

print("First 5 rows:")
print(df.head())

print("\nLast 5 rows:")
print(df.tail())


print(df.describe())