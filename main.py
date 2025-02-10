# coded by Loukrichi Fouad

def vigenere_encrypt(text, key):
    encrypted_text = ""
    key_index = 0
    key = key.upper()
    
    # Loop through every character in the text
    for char in text:
        if char.isalpha() or char.isdigit() or not char.isalnum():  # Include letters, digits, and symbols
            char_value = ord(char)  # Get ASCII value of character
            key_char = key[key_index % len(key)]  # Repeat key if shorter than text
            key_value = ord(key_char)  # Get ASCII value of key character

            # Encrypt the character by shifting its ASCII value
            encrypted_char_value = (char_value + key_value) % 256  # Mod 256 for all ASCII characters
            encrypted_char = chr(encrypted_char_value)  # Convert back to character
            
            encrypted_text += encrypted_char
            key_index += 1  # Move to the next character in the key
        else:
            encrypted_text += char  # Non-alphabetic characters remain unchanged

    return encrypted_text


def vigenere_decrypt(text, key):
    decrypted_text = ""
    key_index = 0
    key = key.upper()
    
    # Loop through every character in the text
    for char in text:
        if char.isalpha() or char.isdigit() or not char.isalnum():  # Include letters, digits, and symbols
            char_value = ord(char)  # Get ASCII value of character
            key_char = key[key_index % len(key)]  # Repeat key if shorter than text
            key_value = ord(key_char)  # Get ASCII value of key character

            # Decrypt the character by shifting its ASCII value
            decrypted_char_value = (char_value - key_value + 256) % 256  # Mod 256 for all ASCII characters
            decrypted_char = chr(decrypted_char_value)  # Convert back to character
            
            decrypted_text += decrypted_char
            key_index += 1  # Move to the next character in the key
        else:
            decrypted_text += char  # Non-alphabetic characters remain unchanged

    return decrypted_text



# Input text and key
initial_text = input("Enter the text to encrypt: ")
key = input("Enter the key: ")

# Encrypt the text
encrypted_text = vigenere_encrypt(initial_text, key)
print("Encrypted Text:", encrypted_text)

# Decrypt the text
decrypted_text = vigenere_decrypt(encrypted_text, key)
print("Decrypted Text:", decrypted_text)
