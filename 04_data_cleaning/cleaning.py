import pandas as pd

df = pd.read_csv("hw_200.csv")

# Show the missing values

print("Missing Valuse per columns: ")
print(df.isnull().sum())


# Deleting empty rows

df_cleaned = df.dropna()

# or filling empty valuse

df.fillna(0,inplace=True)

# Columns rename

df.rename(columns={"Height(inches)":"Height", "Weight(pounds)":"Weight"}, inplace=True)

# Sorting

df_sorted = df_cleaned.sort_values("Height(inches)")

# First 5 rows after Sorting