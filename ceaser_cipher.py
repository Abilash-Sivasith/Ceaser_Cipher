"""
function to encode the provided text using the ceaser cipher technique

by Abilash Sivasith

"""

ALPHABET =  ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def ceaser_cipher_encryption(plaintext, shift):
    """encrypts provided sentance"""
    encrypted_sentance = ''
    individual_words = plaintext.split(' ')
    word_to_encrpyt_list = []
    blank_space = ' '
    for letters in plaintext:
        if plaintext != blank_space:
            index_of_letter = ALPHABET.index(letters)
            encrypted_index_of_letter = (index_of_letter + shift) % 26 
            letter_of_enctypted_value = ALPHABET[encrypted_index_of_letter]
            encrypted_sentance += str(letter_of_enctypted_value) +  ' '
    return encrypted_sentance

# TESTING - ceaser_cipher_encryption function

# text_to_encrypt = 'ABCD'
# encrypted_code = ceaser_cipher_encryption(text_to_encrypt, 2)
# print(encrypted_code)


