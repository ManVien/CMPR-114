# Project #1 (Writing and Reading files)
# This program writes to a file
def write():
    outFile = open('myFile.txt','w') # writing to the default directory
    outFile1 = open('C:\\Users\\manvi\\Downloads\\File\\myFile.txt','w') # writing to a specific directory

    outFile.write('Jason\n')
    outFile.write('Jill\n')
    outFile.write('Jake\n')

    outFile1.write('Jason\n')
    outFile1.write('Jill\n')
    outFile1.write('Jake\n')

    outFile.close()
    outFile1.close()

    print('the names have been recorded.')

write()
