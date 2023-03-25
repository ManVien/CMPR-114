# This program opens an output file with the filename things.txt, 
# writes the name of an animal, a fruit, and a country to the file
# on separate lines, then closes the file.

def write():
    animal = input('Enter the name of an animal: ')
    fruit = input('Enter the name of a fruit: ')
    country = input('Enter the name of a country: ')

    outfile = open("things.txt","a")

    outfile.write(animal + '\n')
    outfile.write(fruit + '\n')
    outfile.write(country + '\n')

    outfile.close()

    print('data recorded.')

write()

