# Testing Boolean conditions

# Set variables
name = "Dean"

# Create Boolean if statement using the len() function to check string values --> int
if len(name) < 3:
    print("Error: Name must be at least 3 characters long")
elif len(name) > 50:
    print("Error: Name can be a maximum of 50 characters long.")
else:
    print("Name looks good!")