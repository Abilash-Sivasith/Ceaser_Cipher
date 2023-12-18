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
            index_of_letter = ALPHABET.index(letters.upper())
            encrypted_index_of_letter = (index_of_letter + shift) % 26 
            letter_of_enctypted_value = ALPHABET[encrypted_index_of_letter]
            encrypted_sentance += str(letter_of_enctypted_value) +  ' '
    return encrypted_sentance

# TESTING - ceaser_cipher_encryption function
text_to_encrypt = 'Hello World'
encrypted_code = ceaser_cipher_encryption(text_to_encrypt, 8)
print(encrypted_code)

######################################################################################

def ceaser_cipher_decrypter(encrypted_text, shift):
    '''decrypts an encrypted text when you know what shift is being used'''
    deciphered_text = ''
    for letters in encrypted_text:
        if letters != BLANK_SPACE:
            index_of_letter = ALPHABET.index(letters.upper())
            decrypted_index_of_letter_index = (index_of_letter - shift) % 26 
            if decrypted_index_of_letter_index < 0:
                decrypted_index_of_letter_index += 26 
            letter_of_enctypted_value = ALPHABET[decrypted_index_of_letter_index]
            deciphered_text += str(letter_of_enctypted_value) +  ' '
    return deciphered_text

# TESTING - ceaser_cipher_decryption function
#encrypted_text = 'Hello World'
#deciphered_text = ceaser_cipher_decrypter(encrypted_text, 2)
#print(deciphered_text)

######################################################################################

def ceaser_cipher_decryption_guesser(cipher_text):
    '''allows the user to enter a number and see if the text revelled is decrpyted'''
    user_input = (input('Ceaser Shift to Try (enter a num between 0 and 25, inclusive): '))    
    if user_input == 'terminate':
        print('PROGRAM HAS FINNISHED EXACUTING')
        print('This Could be Due to not entering a Valid Int\nOR because you have purpossfully closed the program')     
        return 'Completted'
    user_input = int(user_input)
    if user_input < 26 and user_input >= 0:
        print('trying a shift of ' + str(user_input))
        print(ceaser_cipher_decrypter(cipher_text, user_input))
        print('upto here')
        ceaser_cipher_decryption_guesser(cipher_text)
    elif user_input >= 26 or user_input < 0:
        print('YOU MUST ENTER A VALUE BETWEEN 0 AND 26')
        ceaser_cipher_decryption_guesser(cipher_text)
    
    
# TESTING - ceaser_cipher_decryption_guesser function 
# test_cipher = 'P M T T W E W Z T L'
# test_decrpytion = ceaser_cipher_decryption_guesser(test_cipher)
# print(test_decrpytion)