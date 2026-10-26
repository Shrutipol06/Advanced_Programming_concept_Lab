import pandas as pd
from datetime import date

# Read CSV file
df = pd.read_csv(r"C:\Users\shrut\OneDrive\Desktop\Python\Pandas\age.csv")

# Convert Birthdate to date format
df["Birthdate"] = pd.to_datetime(df["Birthdate"])

# Get system date
today = date.today()

# Calculate age
df["Age"] = df["Birthdate"].apply(
    lambda x: today.year - x.year -
    ((today.month, today.day) < (x.month, x.day))
)

# Display the data
print("Student Details:")
print(df)