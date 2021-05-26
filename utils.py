# Create a utility module class to use in other application files

# Define the method
def find_max_number(numbers):
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number

