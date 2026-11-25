
print("Name: Rathod Ankitha  \nEnrollment: 92600565030")

import re

text = "My enrollment number is 92600565030."

pattern = r"\d+"

result = re.findall(pattern, text)

print("Numbers found in the text:", result)
