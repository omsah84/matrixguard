# Function to convert the plaintext message to ASCII
def text_to_ascii(plaintext):
    return [ord(char) for char in plaintext]

# Function to convert ASCII values back to text
def ascii_to_text(ascii_values):
    # Round and filter values to ensure they convert correctly to characters
    return ''.join([chr(round(val)) for val in ascii_values if round(val) > 0])
