# coded by Loukrichi Fouad

# Encryption formula
## get the asci value for the text
## get the ascii value for the key 
## encryption formula ((text ascii value + key char ascii value) % 256) 
## after you get the number 

# Decryption formula
# (encrypted_char - key_char + 256) % 256


def vigenere_encrypt(text, key):
    encrypted_text = ""
    key_index = 0
    key = key.upper()
    
  
    for char in text:
        if char.isalpha() or char.isdigit() or not char.isalnum():  
            char_value = ord(char) 
            key_char = key[key_index % len(key)] 
            key_value = ord(key_char) 

            
            encrypted_char_value = (char_value + key_value) % 256  
            encrypted_char = chr(encrypted_char_value)  
            
            encrypted_text += encrypted_char
            key_index += 1 
        else:
            encrypted_text += char  

    return encrypted_text


def vigenere_decrypt(text, key):
    decrypted_text = ""
    key_index = 0
    key = key.upper()
    
  
    for char in text:
        if char.isalpha() or char.isdigit() or not char.isalnum(): 
            char_value = ord(char)  
            key_char = key[key_index % len(key)]  
            key_value = ord(key_char)  

           
            decrypted_char_value = (char_value - key_value + 256) % 256 
            decrypted_char = chr(decrypted_char_value)  
            
            decrypted_text += decrypted_char
            key_index += 1 
        else:
            decrypted_text += char  

    return decrypted_text



initial_text = input("Enter the text to encrypt: ")
key = input("Enter the key: ")


encrypted_text = vigenere_encrypt(initial_text, key)
print("Encrypted Text:", encrypted_text)


decrypted_text = vigenere_decrypt(encrypted_text, key)
print("Decrypted Text:", decrypted_text)
