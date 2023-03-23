# Project #1 (Writing and Reading files)
# This program reads from a file
def read():
    infile = open('myFile.txt','r')
    infile1 = open('C:\\Users\\manvi\\Downloads\\File\\myFile.txt','r')

    fileContents = infile.read()
    fileContents1 = infile1.read()

    infile.close()
    infile1.close()

    print(fileContents)
    print(fileContents1)

read()
