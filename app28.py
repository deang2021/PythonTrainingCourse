# Working with inheritance

# Create parent and inheritable class Animal
class Animal:
    def walk(self):
        print("I am walking")


# Create inherited class
class Dog(Animal):
    # pass  This means nothing
    def bark(self):
        print("BARK!")


class Cat(Animal):
    def meow(self):
        print("MEOW!")

# Create object of Dog() and print statement
dog1 = Dog()
dog1.walk()
dog1.bark()

# Create Cat object and print cat specific methods
cat1 = Cat()
cat1.meow()