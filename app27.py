# Further testing of Constructor classes and objects

# Create the class
class User:
    # Create constructor method name
    def __init__(self, name):
        self.name = name

    # Create a welcome method
    def welcome(self):
        print(f"Hi, my name is {self.name}!")


# Create object and print details
user1 = User("Dean G")
user1.welcome()

# Create a new and separate user
user2 = User("Darragh B")
user2.welcome()