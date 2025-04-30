def is_pangram(s):
    # Convert the string to lowercase to handle both uppercase and lowercase
    s = s.lower()
    
    # Create a set to store unique alphabetic characters
    letters = set()
    
    # Loop through each character in the string
    for char in s:
        # If the character is an alphabet letter, add it to the set
        if char.isalpha():
            letters.add(char)
    
    # Check if the set has 26 unique letters
    if len(letters) == 26:
        return "PANGRAM"
    else:
        return "NOT PANGRAM"

sentence = input("Enter the sentence : ")
print(is_pangram(sentence))
