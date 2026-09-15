#Name: KARTHIK DORAPALLY
#Enrollment: 92600565023

#Q.20(a) Python Program to show method overloading by adding two numbers and three numbers using the same method name

print("Name: KARTHIK DORAPALLY \nEnrollment: 92600565023")

class Addition:

    def add(self, num1, num2, num3=0):
        print("The addition is: ", num1 + num2 + num3)

addition = Addition()

addition.add(10, 20)

addition.add(10, 20, 30)