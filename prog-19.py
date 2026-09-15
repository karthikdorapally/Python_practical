#Name: KARTHIK DORAPALLY
#Enrollment: 92600565023

#Q.19 Python Program to demonstrate various types of methods

print("Name: KARTHIK DORAPALLY \nEnrollment: 92600565023")

class Student:

    def instance_method(self):
        print("This is an instance method")

    @classmethod
    def class_method(cls):
        print("This is a class method")

    @staticmethod
    def static_method():
        print("This is a static method")

student1 = Student()

student1.instance_method()

Student.class_method()

Student.static_method()