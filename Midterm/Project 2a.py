# This program will read the coffee text file
# and display the entire file on the console.

def read():
    try:
        infile = open('coffee.txt','r')

        fileContents = infile.read()

        infile.close()

        print(fileContents)

    except Exception as err: # built-in Exception error processing
            print(err)

read()