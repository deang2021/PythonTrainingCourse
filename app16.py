# Utilizing Nested loops

# Second iteration of outer loop
for x in range (4):

    # Control goes back to line 2 until the range function completes
    for y in range(3):
        print(f'({x}, {y})')

# Declare variables
numbers = [5, 2, 5, 2, 2]

# Create For loop
for x_count in numbers:

    # Set variable output
    output = ''

    # Set for loop to print x
    for count in range(x_count):
        output += 'x'
    print(output)
