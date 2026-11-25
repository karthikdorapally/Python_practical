print("Name: Rathod Ankitha  \nEnrollment: 92600565030")

# Write mode
file = open("demo.txt", "w")
file.write("This is the first line.\n")
file.close()

# Append mode
file = open("demo.txt", "a")
file.write("This is the second line.\n")
file.close()

# Read mode
file = open("demo.txt", "r")
print("File Content:")
print(file.read())
file.close()
