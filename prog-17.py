#Name: KARTHIK DORAPALLY
#Enrollment: 92600565023

#Q.17 Python Program to demonstrate the concept of inner class

print("Name: KARTHIK DORAPALLY \nEnrollment: 92600565023")

class Student:
    def display(self):
        print("This is the Student class")

    class Address:
        def display_address(self):
            print("City: Ahmedabad")
            print("Country: India")

student1 = Student()
student1.display()

address1 = student1.Address()
address1.display_address()