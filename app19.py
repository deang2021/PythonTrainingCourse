# Working with List Methods

# Set a list
numbers = [5, 5, 3, 9, 7]

# Call a method to add to the list
numbers.append(3)
print(numbers)

# Call a sort method to sequentially call the list
numbers.sort()
print(numbers)

# Copy the original list
numbers2 = numbers.copy()

# Remove duplicate values from a List
numbers = [2, 2, 4, 6, 3, 4, 6, 1]

# Create a unique List
uniqueValues = []

# For loop to iterate
for number in numbers:

    # If number not in unique list, add it. If it is there already, it will not be added.
    if number not in uniqueValues:
        uniqueValues.append(number)
print(uniqueValues)