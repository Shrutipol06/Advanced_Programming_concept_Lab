import pandas as pd

data = pd.read_csv(r"C:\Users\shrut\OneDrive\Desktop\Python\Pandas\students.csv")

series = data["Name"]

print("Series:")
print(series)