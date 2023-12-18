"""
function to encode the provided text using the ceaser cipher technique
function to decode the provided cipher text using the ceaser cipher technique
function to allow user to input a number and see if the resulting text is decrypted

by Abilash Sivasith

"""

ALPHABET =  ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
BLANK_SPACE = ' '

def ceaser_cipher_encryption(plaintext, shift):
    """encrypts provided sentance"""
    encrypted_sentance = ''
    for letters in plaintext:
        if letters != BLANK_SPACE:
            index_of_letter = ALPHABET.index(letters)
            encrypted_index_of_letter = (index_of_letter + shift) % 26 
            letter_of_enctypted_value = ALPHABET[encrypted_index_of_letter]
            encrypted_sentance += str(letter_of_enctypted_value) +  ' '
    return encrypted_sentance

# TESTING - ceaser_cipher_encryption function
#text_to_encrypt = 'A B C D'
#encrypted_code = ceaser_cipher_encryption(text_to_encrypt, 1)
#print(encrypted_code)

######################################################################################

def ceaser_cipher_decrypter(encrypted_text, shift):
    '''decrypts an encrypted text when you know what shift is being used'''
    deciphered_text = ''
    for letters in encrypted_text:
        if letters != BLANK_SPACE:
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

######################################################################################

def ceaser_cipher_decryption_guesser(cipher_text):
    '''allows the user to enter a number and see if the text revelled is decrpyted'''
    user_input = input('Ceaser Shift to Try, enter ' ' to stop: ')
    user_input = int(user_input)
    if user_input != int:
        print('Please enter a number between 0 and 26')
        ceaser_cipher_decryption_guesser(cipher_text)
    blank_space = ' '


    while user_input != blank_space:
        ceaser_cipher_decrypter(cipher_text, user_input)

user_input = int(input('you moron'))
if type(user_input) == int:
    print('True')