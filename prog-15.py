#Name: KARTHIK DORAPALLY
#Enrollment: 92600565023

#Q.15 Python Program to demonstrate the use of various arguments which can be passed to functions

print("Name: KARTHIK DORAPALLY \nEnrollment: 92600565023")

def student(name, age=21):
    print("Student Name is: ", name)
    print("Student Age is: ", age)

print("Using positional arguments:")
student("Aman", 21)

print("Using keyword arguments:")
student(age=22, name="Rahul")

print("Using default arguments:")
student("Karan")