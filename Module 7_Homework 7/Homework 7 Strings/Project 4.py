# Pig Latin
# This program accepts a sentence as input and converts each word to “Pig Latin.” 
# In one version, to convert a word to Pig Latin, you remove the first letter and place that letter
# at the end of the word. Then, you append the string “ay” to the word. Here is an example:
# English: I SLEPT MOST OF THE NIGHT
# Pig Latin: IAY LEPTSAY OSTMAY FOAY HETAY IGHTNAY

def main():
    # Get a sentence from user
    string = input('Enter a sentence: ')
    print('Pig Latin:',get_pig_latin(string))

def get_pig_latin(string):
    string = string.upper()
    word_list = string.split()      # return a list containing the words in the string
    pig_latin = ''

    try:
        for word in word_list:          # loop each word in the word_list
            pig_latin += word[1:] + word[0] + 'AY '   # remove the first letter, place that letter at the end 
                                                      # of the word, and append the string “ay” to the word
        return pig_latin

    except Exception as err:  # built-in Exception error processing
        print(err)

main()
