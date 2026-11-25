print("Name: Rathod Ankitha \nEnrollment: 92600565030")

# Single Inheritance

class Animal:

    def eat(self):
        print("Animal can eat")


class Dog(Animal):

    def bark(self):
        print("Dog can bark")


# Multilevel Inheritance

class Puppy(Dog):

    def play(self):
        print("Puppy can play")


# Hierarchical Inheritance

class Cat(Animal):

    def meow(self):
        print("Cat can meow")


print("\nSingle Inheritance:")

dog = Dog()
dog.eat()
dog.bark()


print("\nMultilevel Inheritance:")

puppy = Puppy()
puppy.eat()
puppy.bark()
puppy.play()


print("\nHierarchical Inheritance:")

cat = Cat()
cat.eat()
cat.meow()