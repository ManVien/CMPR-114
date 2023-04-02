# Vowels and Consonants
# This program has a function that accepts a string as an argument
# and returns the number of vowels that the string contains. 
# It also has another function that accepts a string as an argument 
# and returns the number of consonants that the string contains. 
# This program should let the user enter a string and display the number
# of vowels and the number of consonants it contains.

def main():
    # let the user enter a string
    string = input('Enter a string: ')
    
    # display the number of vowels and the number of consonants it contains.
    print('The number of vowels', get_vowels(string))
    print('The number of consonants', get_consonants(string))


# get_vowels function accepts a string as an argument and 
# returns the number of vowels that the string contains. 
def get_vowels(string):
    number_vowels = 0
    vowelList = ['a','e','i','o','u']
    for char in string:
        if char.lower() in vowelList:
            number_vowels += 1

    return number_vowels
    
# get_consonants function accepts a string as an argument and
# returns the number of consonants that the string contains. 
def get_consonants(string):
    number_consonants = 0
    vowelList = ['a','e','i','o','u']
    string1 = string.lower()
    for char in string1:
        if char not in vowelList:
            if char > 'a' and char <= 'z':
                number_consonants += 1

    return number_consonants
    
main()


