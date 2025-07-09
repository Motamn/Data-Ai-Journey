import pandas as pd

df = pd.read_csv("hw_200.csv")

print("First 5 Rows: ")
print(df.head())

print("Info: ")
df.info()

print("Some analysis: ")
print(df.describe())

print("Empty values: ")
print(df.isnull().sum())