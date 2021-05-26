# Building a guessing game using a while loop

# Define variables and increment
secretNumber = 8
guessCount = 0
guessLimit = 3

# Set a welcome and instruction message
print("---Guessing Game---")
print(" You have 3 attempts to guess the number between 1-10. Good luck!")
print("   ")

# Set while loop and request user input
while guessCount < guessLimit:
    userGuess = int(input('Guess: '))
    guessCount += 1

    # Set the if condition
    if userGuess == secretNumber:
        print(f"SUCCESS! You have guessed the correct secret number {secretNumber}!")
        # Terminate the loop if successful
        break

# Set the condition if the user does not input the correct number
else:
    print("Sorry, you have failed to guess the correct number!")