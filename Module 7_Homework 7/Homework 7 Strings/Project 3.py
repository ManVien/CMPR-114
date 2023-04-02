# Word Separator
# This program accepts as input a sentence in which all of the words are run together,
# but the first character of each word is uppercase. Convert the sentence to a string in which
# the words are separated by spaces, and only the first word starts with an uppercase letter. 
# For example the string “StopAndSmellTheRoses.” would be converted to “Stop and smell
# the roses.”

def main():
    # Get a sentence from the user
    string = input('Enter a sentence in which all of the words are run together,\n' 
                'and the first character of each word is uppercase: \n')
    print('The string after conversion:', get_spaces_and_lowercase(string))
    
def get_spaces_and_lowercase(string):
    count = 0
    new_string = ''
    
    try:
        for ch in string: # loop the characters of string, one by one
            if ch.isupper() and count > 0:  # uppercase character and not the first character
                new_string += " "   # ensures a space is inserted before each uppercase character
                new_string += ch.lower()    # lower the character
            else:       # the first uppercase character or lowercase character
                new_string += ch
            count += 1  # control characters added to the new string

        return new_string

    except Exception as err:  # built-in Exception error processing
        print(err)

main()
