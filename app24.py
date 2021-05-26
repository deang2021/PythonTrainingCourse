# Reusing the Emoji Convertor as a function

# Create function for one task only taking parameter mood
def emoji_convertor(mood):

    # Split input from the user from the split() function
    words = mood.split(' ')

    # Declare emoji list and equal them from text format => emoji format
    emojis = {
        ":)": "😊",
        ":(": "☹",
    }

    # Create a for loop to check emoji list
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


# Request a variable from the user
mood = input("Please enter if you are feeling happy or sad > ")

# Return the function and passed aruegement via placeholder mood
print(emoji_convertor(mood))