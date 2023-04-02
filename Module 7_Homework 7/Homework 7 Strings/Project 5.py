# Caesar Cipher
# A “Caesar Cipher” is a simple way of encrypting a message by replacing each letter with a
# letter a certain number of spaces up the alphabet. For example, if shifting the message by
# 13, an A would become an N, while an S would wrap around to the start of the alphabet
# to become an F.
# This program asks the user for a message (a string) and a shift amount (an integer).
# The values should be passed to a function that accepts a string and an integer as arguments, 
# and returns a string representing the original string encrypted by shifting the letters by the integer. 
# For example, a string of “BEWARE THE IDES OF MARCH” and an integer of 13 
# should result in a string of “ORJNER GUR VQRF BS ZNEPU”.

def main():
    try:
        string = input('Enter a string: ')
        shift_amount = int(input('Enter a shift amount: '))
        print('The encrypted string is:',get_caesar_cipher(string, shift_amount))

    except Exception as err:  # built-in Exception error processing
        print(err)

def get_caesar_cipher(string, shift_amount):
    encrypted_string = ''
    new_word = ''
    string1 = string.upper()
    word_list = string1.split() 

    try:
        for word in word_list:
            for char in word:
                # find the position of character in the alphabet 
                char_position = ord(char) - ord('A')

                # perform the shift
                new_char_position = (char_position + shift_amount) % 26

                # convert to new character
                new_char_decimal = new_char_position + ord('A')        
                new_char = chr(new_char_decimal)

                # append new character to new word
                new_word += new_char

            # append new word to encrypted string
            encrypted_string += new_word + ' '

            # set the new_word variable back to empty string
            new_word = ''

        if string.islower():
            encrypted_string = encrypted_string.lower()
        else:
            encrypted_string

        return encrypted_string

    except Exception as err:  # built-in Exception error processing
        print(err)

main()