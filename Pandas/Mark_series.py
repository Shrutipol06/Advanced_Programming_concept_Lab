import pandas as pd

series = pd.read_csv(r"C:\Users\shrut\OneDrive\Desktop\Python\Pandas\students.csv", usecols=["Marks"]).squeeze("columns")

print("Marks Series:")
print(series)