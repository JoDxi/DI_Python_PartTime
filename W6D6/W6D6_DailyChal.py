# Daily Challenge - Caesers Cipher

import string

def caesar(text, shift, alphabets):
    def shift_alphabet(alphabet):
        return alphabet[shift:] + alphabet[:shift]

    shifted_alphabets = tuple(map(shift_alphabet, alphabets))
    final_alphabet = ''.join(alphabets)
    final_shifted_alphabet = ''.join(shifted_alphabets)
    table = str.maketrans(final_alphabet, final_shifted_alphabet)
    return text.translate(table)

user_choice = input(str('Would you like to ecnrypt or decrypt? '))

if user_choice == 'encrypt':
    plain_text = input(str('Please type the message you would like to encrypt '))
    print(caesar(plain_text, 3, [string.ascii_lowercase, string.ascii_uppercase, string.punctuation]))

elif user_choice == 'decrypt':
    plain_text = input(str('Please type the message you would like to decrypt '))
    print(caesar(plain_text, 26 - 3, [string.ascii_lowercase, string.ascii_uppercase, string.punctuation]))