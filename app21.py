# Emoji convertor program

# Request a variable from the user
mood = input("Please enter if you are feeling happy or sad > ")

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

print(output)

