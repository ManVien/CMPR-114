# This program opens an output file with the filename number_list.txt, 
# uses a loop to write the numbers 1 through 100 to the file, then closes 
# the file.

def write():
    outfile = open('number_list.txt','w')

    for num in range(1,101):
        outfile.write(str(num) + '\n')

    outfile.close()

    print('data recorded.')

write()

