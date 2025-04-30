# Ask the user to enter a word
word = input("Enter a word: ")

# Capitalize every other letter
modified_word = "".join(
    letter.upper() if i % 2 else letter.lower() for i, letter in enumerate(word)
)

# Display the result
print("Modified word:", modified_word)
