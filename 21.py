print("Name: Rathod Ankitha \nEnrollment: 92600565030")

class Animal:

    def eat(self):
        print("Animal can eat")


class Dog(Animal):

    def bark(self):
        print("Dog can bark")


dog = Dog()

dog.eat()
dog.bark()