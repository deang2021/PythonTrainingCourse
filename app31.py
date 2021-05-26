# Creating an application using the random function built-in to python

# Import the built-in Random function
import random

# Create a for loop ti iterate the random value 3 times
for i in range(3):
    print(random.randint(10, 20))

# Create a further example with a List to randomly select
users = ['Dean', 'John', 'Berry']
# Print the result
selected_user = random.choice(users)

# Create a dice game using the random import


class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second

# Create dice object and output method


dice = Dice()
print(dice.roll())

