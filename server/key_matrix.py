import numpy as np

# Function to generate a random key matrix based on plaintext length
def generate_random_key_matrix(length):
    # The size of the key matrix should match the number of characters in the plaintext (assuming 2x2 matrix for simplicity)
    size = int(np.ceil(np.sqrt(length)))  # Find the size of the square matrix
    key_matrix = np.random.randint(1, 10, (size, size))  # Generate random integers between 1 and 9
    return key_matrix
