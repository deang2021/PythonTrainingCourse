# Working with 2D Lists

# Define a matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

# Print the matrix using index places - should print 2
print(matrix[0][1])

# Print all the items in the matrix list using for loop
for row in matrix:
    for item in row:
        print(item)