import string
import random

# Define the file path and size in bytes
file_path = "output100mbjustletters.txt"
file_size = 100 * 1024 * 1024  # 100 MB

# Define the characters to use in the text
characters = string.ascii_letters

# Open the file in append mode
with open(file_path, "a") as f:
    # Loop until the file reaches the desired size
    while f.tell() < file_size:
        # Generate a random string of characters
        text = ''.join(random.choice(characters) for _ in range(1024))
        # Append the text to the file
        f.write(text)
