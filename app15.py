# Learning about for loops

# Create for loop with variable item
for item in 'Python':
    print(item)

# Create a name loop
for name in ['Dean', 'John', 'Shane']:
    print(name)

# Create a number for loop with range function (will not include 10)
for numbers in range(5, 10, 2): # Use 2 to skip
    print(numbers)

# Create an array of integers
prices = [10, 20, 30]
total = 0

# Create a for loop to iterate values
for price in prices:
    total += price # add all values together

print(f'Total: {total}')