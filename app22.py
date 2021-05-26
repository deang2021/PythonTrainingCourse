# Working with Functions

# Create function using def - functions should always be lower case
def greet_customer():
    print('Hello!')
    print('Welcome to Croke Park!')


# Print the function
print("Start")
greet_customer()
print("Finish")


# Create a function and pass two parameters to it
def greet_customer_name(first_name, last_name):
    print(f'Hello, {first_name} {last_name}.')
    print('Welcome to Croke Park!')


# Print the function
print("Start")
greet_customer_name("John", "Smith")
greet_customer_name("Mary", "Smith")
print("Finish")
