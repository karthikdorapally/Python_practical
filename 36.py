# Q.36 Python Program to demonstrate different ways of creating DataFrames
print("Name: Rathod Ankitha  \nEnrollment: 92600565030")

import pandas as pd

# Method 1: Using Dictionary

data1 = {
    "Name": ["Rathod Ankitha", "nissy"],
    "Age": [22, 21]
}

df1 = pd.DataFrame(data1)

print("DataFrame using Dictionary:")

print(df1)

# Method 2: Using List

data2 = [
    ["karthik", 22],
    ["nissy", 21],
    ["bunny", 23]
]

df2 = pd.DataFrame(data2, columns=["Name", "Age"])

print("\nDataFrame using List:")

print(df2)

# Method 3: Using List of Dictionaries

data3 = [
    {"Name": "Rathod Ankitha ", "Age": 22},
    {"Name": "nissy", "Age": 21}
]

df3 = pd.DataFrame(data3)

print("\nDataFrame using List of Dictionaries:")

print(df3)

# Method 4: Using Series

data4 = {
    "Name": pd.Series(["Rathod Ankitha", "nissy"]),
    "Age": pd.Series([22, 21])
}

df4 = pd.DataFrame(data4)

print("\nDataFrame using Series:")

print(df4)

