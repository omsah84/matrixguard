import numpy as np
from conversion import text_to_ascii

# Function to encrypt the plaintext using the key matrix
def encrypt(plaintext, key_matrix):
    plaintext_ascii = text_to_ascii(plaintext)
    size = len(key_matrix)
    
    # If the plaintext length is not a multiple of the key matrix size, pad with zeroes
    while len(plaintext_ascii) % size != 0:
        plaintext_ascii.append(0)
    
    # Reshape plaintext into a matrix for multiplication
    plaintext_matrix = np.array(plaintext_ascii).reshape((-1, size)).T
    
    # Multiply key matrix by the plaintext matrix
    ciphertext_matrix = np.dot(key_matrix, plaintext_matrix)  # Matrix multiplication
    
    # Return the encrypted values (flattened as a list)
    return ciphertext_matrix.T.flatten().tolist()
