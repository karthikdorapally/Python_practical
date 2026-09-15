#Name: KARTHIK DORAPALLY
#Enrollment: 92600565023

#Q.13 Python Program to demonstrate the use of dictionary and various functions of it

print("Name: KARTHIK DORAPALLY \nEnrollment: 92600565023")

student = {
    "Name": "KARTHIK DORAPALLY",
    "Age": 21,
    "Course": "MSc Cybersecurity"
}

print("The dictionary is: ", student)

print("The keys are: ", student.keys())

print("The values are: ", student.values())

print("The items are: ", student.items())

student["City"] = "Ahmedabad"
print("After adding City: ", student)

student.pop("Age")
print("After removing Age: ", student)

print("The length of dictionary is: ", len(student))