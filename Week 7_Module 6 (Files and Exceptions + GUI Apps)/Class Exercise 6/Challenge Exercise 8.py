# This program writes random numbers from 1-10 into a text file and read the contents.

import random 

def main():
    value = create_random_numbers()
    write(value)
    read()

def create_random_numbers():
    # Create an empty list.
    numbers = []

    # Create and add random numbers to the list.
    for index in range(10):
        numbers.append(random.randint(1,10))

    return numbers

def write(numbers): # write to a file
    try:
        # Open a file in append mode
        outfile = open('random_numbers.txt','a')

        # Write the output to the file
        for count in numbers:
            outfile.write(str(count) + '\n')

        # Close the file
        outfile.close()
        print('data recorded.')
    except Exception as err:  # built-in Exception error processing
        print(err)

def read(): # reading
    print('\nReading the contents from file.')
    try:
        infile = open('random_numbers.txt','r')

        for line in infile:
            print(line.rstrip('\n'))

        infile.close()
    except Exception as err:  
        print(err)

    print()

main()
