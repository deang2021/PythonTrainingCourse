# Working with Dictionaries

# Set customer data using dictionary
customer = {
    "name": "Dean G",
    "age": 24,
    "isVerified": True
}
# Print example
print(customer["name"])

# Also works with get() method
print(customer.get("name"))

# Adding a new value to the dictionary
customer["birthday"] = "July 1 1971"
print(customer["birthday"])

# Build a program to output integer values
phone = input("Phone: ")

# Build a dictionary
digitsMapping = {
    "1": "One ",
    "2": "Two ",
    "3": "Three ",
    "4": "Four ",
}

# Declare looping variable
output = ""

# Use a for loop to check values using variable character
for character in phone:
    output += digitsMapping.get(character, "Integer not known " )
print(output)