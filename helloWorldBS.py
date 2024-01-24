# could you write a very fancy hello world script in python, just to showcase some more cool python/numpy/scipy
# features in one short silly script    

import numpy as np

# Define the message to display
message = "Hello!"

# Convert the message to a NumPy array of characters
chars = np.array(list(message))

# Create a mask for the vowels in the message
vowels = np.isin(chars, list("AEIOUaeiou"))

# Replace the vowels with asterisks
chars[vowels] = "*"

# Print the modified message
print("".join(chars))



