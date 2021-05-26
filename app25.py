# Working with Exceptions (Try and Expect blocks)

# 0 = Successful exit
# 1 = Crash/Fail

# Create try for user input
try:
    age = int(input("Age: "))
    income = 20000
    risk = income / age
    print(age)

# Create the exception error message for ValueError (string input on expected numerical)
except ValueError:
    print("Invalid value")

# Create the exception error message for ZeroDivisionError
except ZeroDivisionError:
    print("Age cannot be 0.")

