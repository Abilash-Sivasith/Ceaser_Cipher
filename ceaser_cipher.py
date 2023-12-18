"""
function to encode the provided text using the ceaser cipher technique
function to decode the provided cipher text using the ceaser cipher technique


by Abilash Sivasith

"""

ALPHABET =  ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def ceaser_cipher_encryption(plaintext, shift):
    """encrypts provided sentance"""
    encrypted_sentance = ''
    blank_space = ' '
    for letters in plaintext:
        if letters != blank_space:
            index_of_letter = ALPHABET.index(letters)
            encrypted_index_of_letter = (index_of_letter + shift) % 26 
            letter_of_enctypted_value = ALPHABET[encrypted_index_of_letter]
            encrypted_sentance += str(letter_of_enctypted_value) +  ' '
    return encrypted_sentance

# TESTING - ceaser_cipher_encryption function
#text_to_encrypt = 'A B C D'
#encrypted_code = ceaser_cipher_encryption(text_to_encrypt, 1)
#print(encrypted_code)

def ceaser_cipher_decrypter(encrypted_text, shift):
    '''decrypts an encrypted text when you know what shift is being used'''
    deciphered_text = ''
    blank_space = ' '
    for letters in encrypted_text:
        if letters != blank_space:
            index_of_letter = ALPHABET.index(letters)
            decrypted_index_of_letter_index = (index_of_letter - shift) % 26 
            if decrypted_index_of_letter_index < 0:
                decrypted_index_of_letter_index += 26 
            letter_of_enctypted_value = ALPHABET[decrypted_index_of_letter_index]
            deciphered_text += str(letter_of_enctypted_value) +  ' '
    return deciphered_text

# TESTING - ceaser_cipher_decryption function
#encrypted_text = 'A B C D'
#deciphered_text = ceaser_cipher_decrypter(encrypted_text, 2)
#print(deciphered_text)