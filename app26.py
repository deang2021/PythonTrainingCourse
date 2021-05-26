# Working with Classes for complex object types

# Create class (note capital letter) - classes always capitals
# Methods and functions use lower-case and underscores
class Point:

    # Define objects
    def move(self):
        print("Move")

    def draw(self):
        print("Draw")

    # Create constructor definition and pass placeholders to be set: x, y
    def __init__(self, x, y):
        self.x = x
        self.y = y


# Create the object
point1 = Point(30, 40)


# Example print statements
point1.x = 50
point1.y = 20
print(point1.x)

# Print message
point1.draw()
point1.move()

# Create separate and new object passing parameters
point = Point(10, 20)
print(point.x)
