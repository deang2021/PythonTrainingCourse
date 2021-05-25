# Working with Lists

# Declare list
names = ['John', ' Berry', 'Dean', 'Dolan', 'Shane']
print(names)

# Use index function to print a particular name or name range
print(names[0:3])

# Append an existing list
names[0] = 'Jon'
print(names)

# Finding the largest item in a list
numbers = [3, 2, 10, 8, 7, 5]

# Set the first number to max as a placeholder/comparison
max = numbers[0]

# Create for loop to iterate through list of numbers
for number in numbers:

    # If new number is greater than 3, set it as new max
    if number > max:
        max = number
print(max)