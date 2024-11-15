from flask import Flask, request, jsonify
import numpy as np
from key_matrix import generate_random_key_matrix
from encryption import encrypt
from decryption import decrypt
from conversion import text_to_ascii
from conversion import ascii_to_text

app = Flask(__name__)

@app.route('/encrypt', methods=['POST'])
def encrypt_message():
    plaintext = request.json.get('plaintext')
    
    # Generate the key matrix based on the length of the plaintext
    key_matrix = generate_random_key_matrix(len(plaintext))
    
    # Encrypt the plaintext using the generated key matrix
    ciphertext =  ascii_to_text(encrypt(plaintext, key_matrix))
    # ciphertext = encrypt(plaintext, key_matrix)
    
    # Return the encrypted message and key matrix
    return jsonify({
        'ciphertext': ciphertext,
        'key_matrix': key_matrix.tolist()
    })

@app.route('/decrypt', methods=['POST'])
def decrypt_message():
    ciphertext = text_to_ascii(request.json.get('ciphertext'))
    # ciphertext = request.json.get('ciphertext')
    key_matrix = np.array(request.json.get('key_matrix'))
    
    # Decrypt the ciphertext using the key matrix
    decrypted_message = decrypt(ciphertext, key_matrix)
    
    return jsonify({'decrypted_message': decrypted_message})

if __name__ == '__main__':
    app.run(debug=True)












































































# from flask import Flask, request, jsonify
# import numpy as np
# import random

# app = Flask(__name__)

# # Function to generate a random key matrix based on plaintext length
# def generate_random_key_matrix(length):
#     # The size of the key matrix should match the number of characters in the plaintext (assuming 2x2 matrix for simplicity)
#     size = int(np.ceil(np.sqrt(length)))  # Find the size of the square matrix
#     key_matrix = np.random.randint(1, 10, (size, size))  # Generate random integers between 1 and 9
#     return key_matrix

# # Function to convert the plaintext message to ASCII
# def text_to_ascii(plaintext):
#     return [ord(char) for char in plaintext]

# # Function to encrypt the plaintext using the key matrix
# def encrypt(plaintext, key_matrix):
#     plaintext_ascii = text_to_ascii(plaintext)
#     size = len(key_matrix)
    
#     # If the plaintext length is not a multiple of the key matrix size, pad with zeroes
#     while len(plaintext_ascii) % size != 0:
#         plaintext_ascii.append(0)
    
#     # Reshape plaintext into a matrix for multiplication
#     plaintext_matrix = np.array(plaintext_ascii).reshape((-1, size)).T
    
#     # Multiply key matrix by the plaintext matrix
#     ciphertext_matrix = np.dot(key_matrix, plaintext_matrix)  # Matrix multiplication
    
#     # Return the encrypted values (flattened as a list)
#     return ciphertext_matrix.T.flatten().tolist()

# # Function to decrypt the ciphertext using the inverse of the key matrix
# def decrypt(ciphertext, key_matrix):
#     # Calculate the inverse of the key matrix
#     try:
#         key_matrix_inv = np.linalg.inv(key_matrix)
#     except np.linalg.LinAlgError:
#         return "Error: Key matrix is not invertible."
    
#     # Reshape ciphertext into a matrix
#     size = len(key_matrix)
#     ciphertext_matrix = np.array(ciphertext).reshape((-1, size)).T
    
#     # Multiply the inverse key matrix by the ciphertext matrix to get the plaintext matrix
#     plaintext_matrix = np.dot(key_matrix_inv, ciphertext_matrix)
    
#     # Flatten the matrix and convert back to ASCII values
#     plaintext_ascii = plaintext_matrix.T.flatten().tolist()
    
#     # Round the values to get back to integers and convert to characters
#     plaintext_chars = ''.join([chr(round(val)) for val in plaintext_ascii if round(val) > 0])
    
#     return plaintext_chars



# @app.route('/encrypt', methods=['POST'])
# def encrypt_message():
#     plaintext = request.json.get('plaintext')
    
#     # Generate the key matrix based on the length of the plaintext
#     key_matrix = generate_random_key_matrix(len(plaintext))
    
#     # Encrypt the plaintext using the generated key matrix
#     ciphertext = encrypt(plaintext, key_matrix)
    
#     # Return the encrypted message and key matrix
#     return jsonify({
#         'ciphertext': ciphertext,
#         'key_matrix': key_matrix.tolist()
#     })

# @app.route('/decrypt', methods=['POST'])
# def decrypt_message():
#     ciphertext = request.json.get('ciphertext')
#     key_matrix = np.array(request.json.get('key_matrix'))
    
#     # Decrypt the ciphertext using the key matrix
#     decrypted_message = decrypt(ciphertext, key_matrix)
    
#     return jsonify({'decrypted_message': decrypted_message})

# if __name__ == '__main__':
#     app.run(debug=True)
