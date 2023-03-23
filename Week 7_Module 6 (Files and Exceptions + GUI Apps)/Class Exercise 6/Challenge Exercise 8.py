# This program writes random numbers from 1-10 into a text file and read the contents.

def main():
    import random 
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    selected = random.choices(numbers, k=3)
    print(selected)

    # Open a file in append mode
    outfile = open('random_numbers.txt','a')

    # Write the output to the file
    for num in selected:
        outfile.write(str(num) + '\n')

    # Close the file
    outfile.close()
    print('data recorded.\n')

    Read()

def Read():

    infile = open('random_numbers.txt','r')

    # Read the first line from the file
    line = infile.readlines()

    infile.close()

    for index in range(len(line)):
        line[index] = line[index].rstrip('\n')

    print(line)

main()
