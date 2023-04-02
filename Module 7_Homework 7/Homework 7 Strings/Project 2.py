# Most Frequent Character
# This program lets the user enter a string and displays the character that appears most frequently in the string.

def main():
    string = input('Enter a string: ')
    print('The character that appears most frequently in the string is',get_most_frequent_character(string))

def get_most_frequent_character(string):
    try:
        most_frequent_char = ''
        count = 0
        total_count = 0
        string1 = string.strip().lower().replace(" ","")

        for char in string1:
            for str in string1:
                if str == char:
                    count += 1
            if count > total_count:
                total_count = count
                most_frequent_char = char
            count = 0

        return most_frequent_char

    except Exception as err:  # built-in Exception error processing
        print(err)

main()
