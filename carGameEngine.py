# Building a car game engine (simple with no GUI)

# Welcome message
print("-----Welcome to the Car Game-----")
print("Enter the value 'help' to learn the commands!")
print("    ") # Break line

# Declare a variable for user input and a boolean value for the conditions
cmd = ""
is_Started = False

# Setup conditional sequence via while loop - setting boolean to True
while True:
    cmd = input("> ").lower()

    # Setup conditional for command values being entered twice
    if cmd == "start":
        if is_Started:
            print("The car is already started!")
        else:
            is_Started = True
            print("Starting the car engine...")

    # Next segment/command of while loop
    elif cmd == "stop":
        if not is_Started:
            print("Car is already stopped!")
        else:
            is_Started = False
            print("Stopping the car now...")

    # Next segment/command of while loop
    elif cmd == "help":
        # Triple quotes to write 3 lines of text
        print("""
Enter 'start' - to start the car.
Enter 'stop' - to stop the car.
Enter 'quit' - to quit the game.
            """)

    # Create a command to break/exit the while loop
    elif cmd == "quit":
        break

    # Final route if computer cannot understand the value entered
    else:
        print("Sorry, I don't understand that command!")
