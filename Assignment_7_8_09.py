import re

def tokenize(text):
    pattern = r"\b[A-Za-z0-9_]+(?:\.[A-Za-z0-9_]+)*@[A-Za-z0-9-]+\.[A-Za-z]{2,6}\b|\bhttps?://[^\s]+|[0-9,./]+\b|[^\w\s]"
    tokens = re.findall(pattern, text)
    return tokens

# User Input
text = input("Enter text to tokenize: ")
tokens = tokenize(text)
print("Tokens:", tokens)
