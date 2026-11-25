print("Name: Rathod Ankitha  \nEnrollment: 92600565030")

file = open("student.txt", "w")

file.write("Name: Rathod Ankitha\n")
file.write("Enrollment: 92600565030\n")

file.close()

file = open("student.txt", "r")

content = file.read()

print("\nFile Content:")
print(content)

file.close()
