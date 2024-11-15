import numpy as np
from conversion import ascii_to_text

# Function to decrypt the ciphertext using the inverse of the key matrix
def decrypt(ciphertext, key_matrix):
    # Calculate the inverse of the key matrix
    try:
        key_matrix_inv = np.linalg.inv(key_matrix)
    except np.linalg.LinAlgError:
        return "Error: Key matrix is not invertible."
    
    # Reshape ciphertext into a matrix
    size = len(key_matrix)
    ciphertext_matrix = np.array(ciphertext).reshape((-1, size)).T
    
    # Multiply the inverse key matrix by the ciphertext matrix to get the plaintext matrix
    plaintext_matrix = np.dot(key_matrix_inv, ciphertext_matrix)
    
    # Flatten the matrix and convert back to ASCII values
    plaintext_ascii = plaintext_matrix.T.flatten().tolist()
    
    # Convert ASCII values back to characters
    return ascii_to_text(plaintext_ascii)
