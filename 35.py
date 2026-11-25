print("Name: Rathod Ankitha  \nEnrollment: 92600565030")

import pandas as pd

data = {
    "Name": ["karthik", "bunny", "nissy"],
    "Age": [22, 21, 23],
    "City": ["Hyderabad", "Miyapur", "Guntur"]
}

df = pd.DataFrame(data)

print("Student DataFrame:")

print(df)

print("\nDataFrame Information:")

print(df.info())

print("\nFirst Two Records:")

print(df.head(2))

