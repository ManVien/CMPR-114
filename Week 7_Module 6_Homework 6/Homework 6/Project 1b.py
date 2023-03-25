# This program opens the things.txt file created by the program in Algorithm Workbench 1,
# reads all of the data from the file before closing it, and then displays the data 
# from the file.

def read():
    infile = open('things.txt','r')

    fileContents = infile.read()

    infile.close()

    print(fileContents)

read()

